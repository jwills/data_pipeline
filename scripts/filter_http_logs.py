#! /usr/bin/env python

# Filter logs produced by urllib3 into a simple list of URLs
# Intended to be used on files generated by the --log-http option for mrtarget

# Usage: filter_logs <log files>

import sys
from urlparse import urlparse

# If this is set to True, remove the query string part of the URL, i.e. the part after /?
STRIP_QUERY = False

urls = []

for filename in sys.argv[1:]:

    with open(filename) as log_file:

        for line in log_file:
            line = line.rstrip()

            # Skip Elasticsearch calls - only works if ES is running on default port
            if ':9200' in line:
                continue

            # Skip 'Starting new'
            if line.startswith('Starting new'):
                continue

            # Line will now be of the form
            # http://rest.ensembl.org:80 "POST /lookup/id HTTP/1.1" 200 35864

            # Strip "
            line = line.replace('"', '')
            parts = line.split()
            if len(parts) != 6:
                continue

            (base, verb, path, protocol, return_code, size) = parts
            url_string = base + path

            if STRIP_QUERY:
                url_parts = urlparse(url_string)
                url_string = url_parts.scheme + '://' + url_parts.netloc + url_parts.path

            urls.append(url_string)

# Output unique list
unique_urls = set(urls)
for url in unique_urls:
    print url



