from pathlib import Path
import json

from prepare.read_darwin import read_darwin

for pport in read_darwin(Path('../data/darwin/1/0/0.darwin')):
    uR = pport.uR
    for s in uR.schedule:
        print(s)