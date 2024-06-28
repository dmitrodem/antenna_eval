#!/usr/bin/env python3

import click
import freecad
import FreeCAD
import importDXF
import Draft

@click.command()
@click.argument("dxf", type = click.Path("r"))
@click.argument("step", type = click.Path())
def export_dxf(dxf, step):
    importDXF.open(dxf)
    Draft.upgrade(FreeCAD.ActiveDocument.Objects, delete=True)
    objs = Draft.upgrade(FreeCAD.ActiveDocument.Objects, delete=True)[0]
    assert(len(objs) == 1)
    objs[0].Shape.exportStep(step)


if __name__ == "__main__":
    export_dxf()
