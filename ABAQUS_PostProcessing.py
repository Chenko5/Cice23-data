from odbAccess import *
from abaqusConstants import *
# from abaqusConstants import *
from part import *
from material import *
from section import *
from optimization import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
# import odbAccess
#
session.viewports['Viewport: 1'].setValues(displayedObject=None)
odb = odbAccess.openOdb(path='Job-2-CONC.odb')
endSet = odb.rootAssembly.instances['PART-1-INSTANCE-CONC']
# Open a file for writing
myFile = open('FileName.txt', 'w+')
myFile.write("# Time Vol Sum ISOL SUM AVG CONCT n n\n")  # Add a newline escape sequence
for step in odb.steps.values():
    numFrame = len(step.frames)
    for fr in range(0, numFrame):
        frame = step.frames[fr]
        Volfield = frame.fieldOutputs['IVOL']
        VolsubField = Volfield.getSubset(region=endSet)
        Sfield = frame.fieldOutputs['ISOL']
        SolsubField = Sfield.getSubset(region=endSet)
        Ssum = 0
        Vsum = 0 
        for num in range(len(VolsubField.values)):
            Volval = VolsubField.values[num].data
            Volsum = Vsum + Volval
            Solval = SolsubField.values[num].data
            Solsum = Solsum + Solval
        AVG = Solsum / Volsum
        frametotalTime = step.totalTime + frame.frameValue
        myFile.write(str(frametotalTime))
        myFile.write(" ")
        myFile.write(str(Vsum))
        myFile.write(" ")
        myFile.write(str(Ssum))
        myFile.write(" ")
        myFile.write(str(AVG))
        myFile.write("\n")
myFile.close()