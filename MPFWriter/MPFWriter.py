import tempfile
import os
import io

from typing import cast
from . import GCodeToMPF

from UM.Application import Application
from UM.Logger import Logger
from UM.Mesh.MeshWriter import MeshWriter #The writer we need to implement.
from UM.MimeTypeDatabase import MimeTypeDatabase, MimeType
from UM.PluginRegistry import PluginRegistry #To get the g-code writer.

class MPFWriter(MeshWriter):

    version = 3

    def __init__(self):
        super().__init__()

    
    def write(self, stream, nodes, mode = MeshWriter.OutputMode.TextMode):

        #Store the g-code from the scene.
        temp_gcode = tempfile.NamedTemporaryFile("w", delete=False)
        gcode_writer = cast(MeshWriter, PluginRegistry.getInstance().getPluginObject("GCodeWriter"))
        success = gcode_writer.write(temp_gcode, None)
        converter = GCodeToMPF.GCodeToMPF()
        if not success: #Writing the g-code failed. 
            self.setInformation(gcode_writer.getInformation())
            return False

        path = os.path.dirname(os.path.abspath(__file__))
        try: 

            head = io.open((str(path) +"/HeadAndEnd/head.txt"), "r", encoding='utf8')
            end = io.open((str(path) + "/HeadAndEnd/end.txt"), "r", encoding='utf8')
        except EnvironmentError as e:
            if head:
                Logger.log("e", "Cannot open or find HeadFile")
            elif end:
                Logger.log("e", "Cannot open or find EndFile")
            else: 
                Logger.log("Something went wrong")
            return False

        try: 
            converter.openFile(temp_gcode.name, stream.name, head, end)
            
            
            
        except EnvironmentError as e:
            if temp_gcode:
                Logger.log("e", "Cannot create temp-File {pathTempFile}".format(temp_gcode=temp_gcode))
            return False

        temp_gcode.close()
        os.remove(temp_gcode.name)


        return True




