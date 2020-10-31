from scholarly import scholarly
import toolz
import pybtex
import pypandoc

google_scholar_ids = [
    '_ItyW58AAAAJ',  # Ieva Kazlauskaite
    'AH5v9Y0AAAAJ',  # Jan Povala
    'BSoawXwAAAAJ',  # Mark Girolami
]

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

all_publications_list = []

# retrieve_all_articles
for author_id in google_scholar_ids:
    author_details_basic = scholarly.search_author_id(author_id, filled=True)
    author_details_publications = author_details_basic.fill(sections=['publications'])
    print(f"Processing {author_details_basic.name}'s publications")
    for pub in author_details_publications.publications:
        all_publications_list.append(pub)


unique_publications = list(toolz.unique(all_publications_list, key=lambda x: x.id_citations))

# remove those that don't have the author or the year and those that are older than 2010
unique_publications = [pub for pub in unique_publications if ('author' in pub.bib.keys() and 'year' in pub.bib.keys() and pub.bib['year'] > '2010')]
sorted_pubs_year = sorted(unique_publications, key=lambda x: x.bib['year'], reverse=True)

publications_md_content = ""
for pub in sorted_pubs_year:
    publications_md_content += f"- {pub.bib['author']} ({pub.bib['year']}), *{pub.bib['title']}*. "

    if 'journal' in pub.bib.keys():
        publications_md_content += f"{pub.bib['journal']}"
        if 'volume' in pub.bib.keys() and 'pages' in pub.bib.keys():
            publications_md_content += f", {pub.bib['volume']}: {pub.bib['pages']}. "
        else:
            publications_md_content += ". "
    elif  'publisher' in pub.bib.keys():
        publications_md_content += f"{pub.bib['publisher']}. "

    if 'url' in pub.bib.keys():
        publications_md_content += f"[{pub.bib['url']}]({pub.bib['url']}). "

    publications_md_content += "\n"




# list_bibtex_strings = []
# for pub in sorted_pubs_year:
#     pub_record = scholarly.search_single_pub(pub.bib['title'])
#     pub_bibtex = pub_record.bibtex()
#     # pub_bib = next(scholarly.search_pubs(pub.bib['title'])).bibtex
#     list_bibtex_strings.append(pub_bibtex)

# bib_file_content = pybtex.format_from_strings(list_bibtex_strings, style='plain')
# publications_md_content = pypandoc.convert_text(source=bib_file_content, to='md', format='latex')
# publications_md_content = publications_md_content.split("\n", 1)[1]


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
