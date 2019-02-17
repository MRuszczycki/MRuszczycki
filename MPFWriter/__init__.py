# Copyright (c) MRuszczycki & Hochschule Birkenfeld
# MPFWriter released since Cura 6.0

from . import MPFWriter


from UM.i18n import i18nCatalog


catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "mesh_writer": {
            "output": [{
                "extension": "mpf",
                "description": catalog.i18nc("@item:inlistbox", "Numeric MPF file"),
                "mime_type": "text/mpf",
                "mode": MPFWriter.MPFWriter.OutputMode.TextMode
            }]
        }
    }

def register(app):
    return {"mesh_writer": MPFWriter.MPFWriter()}