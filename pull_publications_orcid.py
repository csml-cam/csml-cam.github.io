import logging

import orcid
import os
from requests import RequestException
from dotenv import load_dotenv
import requests
import pybtex
import pypandoc
import re
import random
import string
import toolz
from requests.adapters import HTTPAdapter
from urllib3 import Retry

import logging


def doi2bib(doi):
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    url = f"http://dx.doi.org/{doi}"
    headers = {'Accept': 'application/x-bibtex'}
    logging.info(f"Retrieving bibtex from {url}")
    r = http.get(url, headers=headers)

    # r = requests.get(url, headers=headers)
    if r.status_code is not 200:
        logging.info(r)
        raise RequestException("Failed to retrieve BIB for a DOI.")
    return r.text

if __name__ == '__main__':
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    orcid_ids = [
        "0000-0002-5112-7373",  # Jan
        "0000-0002-7503-2117",  # Ioannis
        "0000-0003-3008-253X",  # Mark
        "0000-0001-9690-0887",  # Ieva
    ]
    api = orcid.PublicAPI(os.environ['ORCID_CLIENT_ID'], os.environ['ORCID_CLIENT_SECRET'])
    search_token = api.get_search_token_from_orcid()

    pub_list = []
    for orcid_id in orcid_ids:
        logging.info(f"Downloading publications for ORCID ID: {orcid_id}.")
        query_result = api.read_record_public(orcid_id, 'works', search_token)
        for orcid_entry in query_result['group']:

            put_code = orcid_entry['work-summary'][0]['put-code']

            orcid_full_entry = api.read_record_public(orcid_id, 'work', search_token, put_code=put_code)
            logging.info(orcid_full_entry)

            try:
                year = orcid_full_entry['publication-date']['year']['value']
            except KeyError:
                year = None

            entry_doi = None
            try:
                external_ids = orcid_full_entry['external-ids']['external-id']
                for external_id in external_ids:
                    if external_id["external-id-type"] == "doi":
                        entry_doi = external_id["external-id-value"]
            except (KeyError, TypeError):
                logging.info("Unable to extract DOI.")
            try:
                orcid_bib_style = orcid_full_entry['citation']['citation-type'].lower()
                if orcid_bib_style == 'bibtex':
                    pub_list.append((orcid_id, put_code, year, entry_doi, orcid_full_entry['citation']['citation-value']))
                # key exists in dict
            except (KeyError, TypeError):
                logging.info("No bibtex available, trying DOI lookup.")
                try:
                    if entry_doi is not None:
                        pub_list.append((orcid_id, put_code, year, entry_doi, doi2bib(entry_doi)))
                except RequestException as e:
                    logging.info(f"Problem retrieving BIB details for: {orcid_entry}")
                    logging.info(e)
                    continue

    # Remove duplicated
    attributes_to_check_uniqueness = [
        1, # put codes
        3,
    ]
    for key in attributes_to_check_uniqueness:
        filtered_pub_list = []
        unique_values = set()
        for pub_entry in pub_list:
            if (pub_entry[key] is None) or (not pub_entry[key] in unique_values):
                filtered_pub_list.append(pub_entry)
                if pub_entry[key] is not None:
                    unique_values.add(pub_entry[key])
        pub_list = filtered_pub_list

    pub_list = sorted(pub_list, key=lambda x: x[2], reverse=True)

    list_bibtex_strings = []
    for _, _, _, _, bib_str in pub_list:
        # add random string token to the bib id to prevent any clashes as bibtex is generated from multiple sources
        parsed_bib_re = re.compile(r"^(@[a-z]+\{)([^\,]+)((.*(\n)*.*)*)", re.MULTILINE)

        matched_str = parsed_bib_re.match(bib_str)

        random_token = ''.join(random.choice(string.ascii_letters) for i in range(10))
        bib_str_randomised = f"{matched_str.group(1)}{matched_str.group(2)}{random_token}{matched_str.group(3)}"
        list_bibtex_strings.append(bib_str_randomised)

    # bib_file_content = pybtex.format_from_strings(list_bibtex_strings, style='unsrt')

    publications_md_content = ""
    for bibtex_string in list_bibtex_strings:
        try:
            formated_bib_entry = pybtex.format_from_string(bibtex_string, style='unsrt')
            formatted_md_entry = pypandoc.convert_text(source=formated_bib_entry, to='md', format='latex')
            formatted_md_entry = formatted_md_entry.split("\n", 1)[1]
            publications_md_content += formatted_md_entry
        except Exception:
            logging.info(f"Failing to format: {bibtex_string}")
            continue


    publications_md_file = """---
title: "CSML@Cam - Publications"
layout: gridlay
excerpt: "CSML@Cam - Publications."
sitemap: false
permalink: /publications/
---

# Publications
    """
    publications_md_file += publications_md_content

    text_file = open("./_pages/publications.md", "w")
    text_file.write(publications_md_file)
    text_file.close()

