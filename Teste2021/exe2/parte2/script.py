import requests
import urllib.parse

query = "PREFIX : <http://prc.di.uminho.pt/2021/myfamily#>\nCONSTRUCT { \n ?a :Descendente ?b .\n} WHERE {\n?b :eProgenitorDe ?a . }"

q = urllib.parse.quote_plus(query)
url = "http://localhost:7200/JCR?query=" + q

p = {'Content-type':'application/x-binary-rdf-results-table'}
r = requests.get(url,p)
r.raise_for_status()
print(r.json())

if r.data:
    insert = "http://localhost:7200/JCR/statements?query=INSERT%20DATA%20{"+r.data+"}"

    requests.post(insert)