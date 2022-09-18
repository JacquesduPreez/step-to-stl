from pathlib import Path
import FreeCAD
import Part
import Mesh
import sys


def get_files(path, extensions):
    all_files = []
    for ext in extensions:
        all_files.extend(path.glob(ext))
    return all_files


path = Path.cwd().joinpath('convert')
stepfiles = get_files(path, ('*.[sS][tT][eE][pP]', '*.[sS][tT][pP]'))
stlfiles = get_files(path, ('*.[sS][tT][lL]',))

if not stepfiles:
    print("No step files found in the given folder")
    sys.exit()

stlstems = [i.stem for i in stlfiles]
processfiles = [i for i in stepfiles if i.stem not in stlstems]

print("Processing files:")
for f in processfiles:
    print(f.name)
    filename = f'{f.parent}/{f.name}'
    shape = Part.Shape()
    shape.read(filename)
    doc = App.newDocument('Doc')
    pf = doc.addObject("Part::Feature", "STEPpreview")
    pf.Shape = shape
    stl = f'{f.parent}/{f.stem}.stl'
    Mesh.export([pf], stl)
    print(f'{f.stem}.stl Generated')
