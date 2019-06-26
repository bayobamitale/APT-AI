from stix2 import TAXIICollectionSource
from taxii2client import Server

# Instantiate server and get API Root
server = Server("https://cti-taxii.mitre.org/taxii/")
api_root = server.api_roots[0]

# Print name and ID of all ATT&CK technology-domains available as collections
for collection in api_root.collections:
          print(collection.title + ": " + collection.id)