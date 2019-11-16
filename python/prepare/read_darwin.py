from pathlib import Path

from .schema_v16 import parseString

xml_header = '<?xml version="1.0" encoding="UTF-8"?>'

def read_xml_feed(path: Path, header=xml_header, leave_header=False):
    return [f"{header}\n{xml}" if leave_header else xml for xml in path.read_text().split(header)[1:]]

def read_darwin(path: Path):
    xmls = read_xml_feed(path)
    pports = [parseString(xml, silence=True) for xml in xmls]
    return pports