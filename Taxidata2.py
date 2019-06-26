
# pip install chain ...
from itertools import chain
# pip install filesystemsource
from stix2 import FileSystemSource

fs = FileSystemSource('./cti/enterprise-attack')

def get_all_software(src):
    filts = [
        [Filter('type', '=', 'malware')],
        [Filter('type', '=', 'tool')]
    ]
    return list(chain.from_iterable(
        src.query(f) for f in filts
    ))
    
get_all_software(fs)