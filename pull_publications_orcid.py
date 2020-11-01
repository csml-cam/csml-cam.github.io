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


def doi2bib(doi):
    #
    url = f"http://dx.doi.org/{doi}"
    headers = {'Accept': 'application/x-bibtex'}
    r = requests.get(url, headers=headers)
    if r.status_code is not 200:
        raise RequestException("Failed to retrieve BIB for a DOI.")
    return r.text

if __name__ == '__main__':
    load_dotenv()

    orcid_ids = [
        "0000-0002-5112-7373",  # Jan
        "0000-0002-7503-2117",  # Ioannis
        "0000-0003-3008-253X",  # Mark
        # "0000-0001-6635-3261"
    ]
    api = orcid.PublicAPI(os.environ['ORCID_CLIENT_ID'], os.environ['ORCID_CLIENT_SECRET'])
    search_token = api.get_search_token_from_orcid()

    bibtex_list = []
    for orcid_id in orcid_ids:
        print(f"Downloading publications for ORCID ID: {orcid_id}.")
        query_result = api.read_record_public(orcid_id, 'works', search_token)
        for orcid_entry in query_result['group']:

            put_code = orcid_entry['work-summary'][0]['put-code']
            try:
                year = orcid_entry['work-summary'][0]['publication-date']['year']['value']
            except KeyError:
                year = None

            entry_doi = None
            try:
                external_ids = orcid_entry['external-ids']['external-id']
                for external_id in external_ids:
                    if external_id["external-id-type"] == "doi":
                        entry_doi = external_id["external-id-value"]
            except KeyError:
                print("Unable to extract DOI")

            try:
                orcid_bib_style = orcid_entry['citation']['citation-type'].lower()
                if orcid_bib_style == 'bibtex':
                    bibtex_list.append((orcid_id, put_code, year, entry_doi, orcid_entry['citation']['citation-value']))
                # key exists in dict
            except KeyError:
                # try with the DOI lookup
                try:
                    if entry_doi is not None:
                        bibtex_list.append((orcid_id, put_code, year, entry_doi, doi2bib(entry_doi)))
                except RequestException as e:
                    # build an entry manually
                    print(f"Problem retrieving BIB details for: {orcid_entry}")
                    print(e)
                    continue

    bibtex_list = list(toolz.unique(bibtex_list, key=lambda x : x[1])) # filter duplicates based on put code
    bibtex_list = list(toolz.unique(bibtex_list, key=lambda x: x[3]))  # filter duplicates based on DOI
    bibtex_list = sorted(bibtex_list, key=lambda x: x[2], reverse=True)

    list_bibtex_strings = []
    for _, _, _, _, bib_str in bibtex_list:

        # add random string token to the bib id to prevent any clashes as bibtex is generated from multiple sources
        parsed_bib_re = re.compile(r"^(@[a-z]+\{)([^\,]+)((.*\n.+)+)", re.MULTILINE)
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
            print(f"Failing to format: {bibtex_string}")
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
