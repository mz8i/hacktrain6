from pathlib import Path

from .schema_v16 import parseString

xml_header = '<?xml version="1.0" encoding="UTF-8"?>'

def read_darwin(path: Path):
    xmls = path.read_text().split(xml_header)[1:]
    pports = [parseString(xml, silence=True) for xml in xmls]
    return pports