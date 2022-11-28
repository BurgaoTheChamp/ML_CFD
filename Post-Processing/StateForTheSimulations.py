# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [837, 836]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.25, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.25, 0.0, 2.7990722937493624]
renderView1.CameraFocalPoint = [0.25, 0.0, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.0606719568268421
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(837, 836)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'OpenFOAMReader'
reynolds290foam = OpenFOAMReader(registrationName='Reynolds290.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder290\\Reynolds290.foam')
reynolds290foam.MeshRegions = ['internalMesh']
reynolds290foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds230foam = OpenFOAMReader(registrationName='Reynolds230.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder230\\Reynolds230.foam')
reynolds230foam.MeshRegions = ['internalMesh']
reynolds230foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds110foam = OpenFOAMReader(registrationName='Reynolds110.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder110\\Reynolds110.foam')
reynolds110foam.MeshRegions = ['internalMesh']
reynolds110foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds800foam = OpenFOAMReader(registrationName='Reynolds800.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder800\\Reynolds800.foam')
reynolds800foam.MeshRegions = ['internalMesh']
reynolds800foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds240foam = OpenFOAMReader(registrationName='Reynolds240.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder240\\Reynolds240.foam')
reynolds240foam.MeshRegions = ['internalMesh']
reynolds240foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds120foam = OpenFOAMReader(registrationName='Reynolds120.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder120\\Reynolds120.foam')
reynolds120foam.MeshRegions = ['internalMesh']
reynolds120foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp120 = Calculator(registrationName='Cp120', Input=reynolds120foam)
cp120.ResultArrayName = 'Cp'
cp120.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.036^2)'

# create a new 'OpenFOAMReader'
reynolds700foam = OpenFOAMReader(registrationName='Reynolds700.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder700\\Reynolds700.foam')
reynolds700foam.MeshRegions = ['internalMesh']
reynolds700foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp110 = Calculator(registrationName='Cp110', Input=reynolds110foam)
cp110.ResultArrayName = 'Cp'
cp110.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.033^2)'

# create a new 'OpenFOAMReader'
reynolds300foam = OpenFOAMReader(registrationName='Reynolds300.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder300\\Reynolds300.foam')
reynolds300foam.MeshRegions = ['internalMesh']
reynolds300foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp300 = Calculator(registrationName='Cp300', Input=reynolds300foam)
cp300.ResultArrayName = 'Cp'
cp300.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.090^2)'

# create a new 'OpenFOAMReader'
reynolds400foam = OpenFOAMReader(registrationName='Reynolds400.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder400\\Reynolds400.foam')
reynolds400foam.MeshRegions = ['internalMesh']
reynolds400foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp400 = Calculator(registrationName='Cp400', Input=reynolds400foam)
cp400.ResultArrayName = 'Cp'
cp400.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.120^2)'

# create a new 'Calculator'
cp290 = Calculator(registrationName='Cp290', Input=reynolds290foam)
cp290.ResultArrayName = 'Cp'
cp290.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.087^2)'

# create a new 'OpenFOAMReader'
reynolds220foam = OpenFOAMReader(registrationName='Reynolds220.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder220\\Reynolds220.foam')
reynolds220foam.MeshRegions = ['internalMesh']
reynolds220foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds1000foam = OpenFOAMReader(registrationName='Reynolds1000.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder1000\\Reynolds1000.foam')
reynolds1000foam.MeshRegions = ['internalMesh']
reynolds1000foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds900foam = OpenFOAMReader(registrationName='Reynolds900.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder900\\Reynolds900.foam')
reynolds900foam.MeshRegions = ['internalMesh']
reynolds900foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds180foam = OpenFOAMReader(registrationName='Reynolds180.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder180\\Reynolds180.foam')
reynolds180foam.MeshRegions = ['internalMesh']
reynolds180foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds130foam = OpenFOAMReader(registrationName='Reynolds130.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder130\\Reynolds130.foam')
reynolds130foam.MeshRegions = ['internalMesh']
reynolds130foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds280foam = OpenFOAMReader(registrationName='Reynolds280.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder280\\Reynolds280.foam')
reynolds280foam.MeshRegions = ['internalMesh']
reynolds280foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds210foam = OpenFOAMReader(registrationName='Reynolds210.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder210\\Reynolds210.foam')
reynolds210foam.MeshRegions = ['internalMesh']
reynolds210foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp210 = Calculator(registrationName='Cp210', Input=reynolds210foam)
cp210.ResultArrayName = 'Cp'
cp210.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.063^2)'

# create a new 'Calculator'
cp180 = Calculator(registrationName='Cp180', Input=reynolds180foam)
cp180.ResultArrayName = 'Cp'
cp180.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.054^2)'

# create a new 'Calculator'
cp1000 = Calculator(registrationName='Cp1000', Input=reynolds1000foam)
cp1000.ResultArrayName = 'Cp'
cp1000.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.300^2)'

# create a new 'OpenFOAMReader'
reynolds500foam = OpenFOAMReader(registrationName='Reynolds500.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder500\\Reynolds500.foam')
reynolds500foam.MeshRegions = ['internalMesh']
reynolds500foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp500 = Calculator(registrationName='Cp500', Input=reynolds500foam)
cp500.ResultArrayName = 'Cp'
cp500.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.150^2)'

# create a new 'OpenFOAMReader'
reynolds270foam = OpenFOAMReader(registrationName='Reynolds270.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder270\\Reynolds270.foam')
reynolds270foam.MeshRegions = ['internalMesh']
reynolds270foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds150foam = OpenFOAMReader(registrationName='Reynolds150.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder150\\Reynolds150.foam')
reynolds150foam.MeshRegions = ['internalMesh']
reynolds150foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp220 = Calculator(registrationName='Cp220', Input=reynolds220foam)
cp220.ResultArrayName = 'Cp'
cp220.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.066^2)'

# create a new 'Calculator'
cp130 = Calculator(registrationName='Cp130', Input=reynolds130foam)
cp130.ResultArrayName = 'Cp'
cp130.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.039^2)'

# create a new 'OpenFOAMReader'
reynolds260foam = OpenFOAMReader(registrationName='Reynolds260.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder260\\Reynolds260.foam')
reynolds260foam.MeshRegions = ['internalMesh']
reynolds260foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp280 = Calculator(registrationName='Cp280', Input=reynolds280foam)
cp280.ResultArrayName = 'Cp'
cp280.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.084^2)'

# create a new 'OpenFOAMReader'
reynolds250foam = OpenFOAMReader(registrationName='Reynolds250.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder250\\Reynolds250.foam')
reynolds250foam.MeshRegions = ['internalMesh']
reynolds250foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp270 = Calculator(registrationName='Cp270', Input=reynolds270foam)
cp270.ResultArrayName = 'Cp'
cp270.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.081^2)'

# create a new 'OpenFOAMReader'
reynolds600foam = OpenFOAMReader(registrationName='Reynolds600.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder600\\Reynolds600.foam')
reynolds600foam.MeshRegions = ['internalMesh']
reynolds600foam.CellArrays = ['U', 'p']

# create a new 'OpenFOAMReader'
reynolds170foam = OpenFOAMReader(registrationName='Reynolds170.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder170\\Reynolds170.foam')
reynolds170foam.MeshRegions = ['internalMesh']
reynolds170foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp170 = Calculator(registrationName='Cp170', Input=reynolds170foam)
cp170.ResultArrayName = 'Cp'
cp170.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.051^2)'

# create a new 'OpenFOAMReader'
reynolds140foam = OpenFOAMReader(registrationName='Reynolds140.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder140\\Reynolds140.foam')
reynolds140foam.MeshRegions = ['internalMesh']
reynolds140foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp140 = Calculator(registrationName='Cp140', Input=reynolds140foam)
cp140.ResultArrayName = 'Cp'
cp140.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.042^2)'

# create a new 'Calculator'
cp260 = Calculator(registrationName='Cp260', Input=reynolds260foam)
cp260.ResultArrayName = 'Cp'
cp260.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.078^2)'

# create a new 'Calculator'
cp250 = Calculator(registrationName='Cp250', Input=reynolds250foam)
cp250.ResultArrayName = 'Cp'
cp250.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.075^2)'

# create a new 'Calculator'
cp240 = Calculator(registrationName='Cp240', Input=reynolds240foam)
cp240.ResultArrayName = 'Cp'
cp240.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.072^2)'

# create a new 'Calculator'
cp600 = Calculator(registrationName='Cp600', Input=reynolds600foam)
cp600.ResultArrayName = 'Cp'
cp600.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.180^2)'

# create a new 'Calculator'
cp230 = Calculator(registrationName='Cp230', Input=reynolds230foam)
cp230.ResultArrayName = 'Cp'
cp230.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.069^2)'

# create a new 'OpenFOAMReader'
reynolds100foam = OpenFOAMReader(registrationName='Reynolds100.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder100\\Reynolds100.foam')
reynolds100foam.MeshRegions = ['internalMesh']
reynolds100foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp100 = Calculator(registrationName='Cp100', Input=reynolds100foam)
cp100.ResultArrayName = 'Cp'
cp100.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.03^2)'

# create a new 'OpenFOAMReader'
reynolds160foam = OpenFOAMReader(registrationName='Reynolds160.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder160\\Reynolds160.foam')
reynolds160foam.MeshRegions = ['internalMesh']
reynolds160foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp900 = Calculator(registrationName='Cp900', Input=reynolds900foam)
cp900.ResultArrayName = 'Cp'
cp900.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.270^2)'

# create a new 'OpenFOAMReader'
reynolds200foam = OpenFOAMReader(registrationName='Reynolds200.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder200\\Reynolds200.foam')
reynolds200foam.MeshRegions = ['internalMesh']
reynolds200foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp200 = Calculator(registrationName='Cp200', Input=reynolds200foam)
cp200.ResultArrayName = 'Cp'
cp200.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.060^2)'

# create a new 'Calculator'
cp800 = Calculator(registrationName='Cp800', Input=reynolds800foam)
cp800.ResultArrayName = 'Cp'
cp800.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.240^2)'

# create a new 'Calculator'
cp150 = Calculator(registrationName='Cp150', Input=reynolds150foam)
cp150.ResultArrayName = 'Cp'
cp150.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.045^2)'

# create a new 'Calculator'
cp160 = Calculator(registrationName='Cp160', Input=reynolds160foam)
cp160.ResultArrayName = 'Cp'
cp160.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.048^2)'

# create a new 'Calculator'
cp700 = Calculator(registrationName='Cp700', Input=reynolds700foam)
cp700.ResultArrayName = 'Cp'
cp700.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.210^2)'

# create a new 'OpenFOAMReader'
reynolds190foam = OpenFOAMReader(registrationName='Reynolds190.foam', FileName='C:\\Users\\dedea\\Documents\\Coding\\My Projects\\CFD_ML\\SImulations\\Cylinder190\\Reynolds190.foam')
reynolds190foam.MeshRegions = ['internalMesh']
reynolds190foam.CellArrays = ['U', 'p']

# create a new 'Calculator'
cp190 = Calculator(registrationName='Cp190', Input=reynolds190foam)
cp190.ResultArrayName = 'Cp'
cp190.Function = '(p*1.225+0.5*1.225*mag(U)^2)/(0.5*1.225*0.057^2)'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cp300
cp300Display = Show(cp300, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Cp'
cpLUT = GetColorTransferFunction('Cp')
cpLUT.AutomaticRescaleRangeMode = 'Never'
cpLUT.RGBPoints = [-0.9, 0.278431372549, 0.278431372549, 0.858823529412, -0.5568000000000002, 0.0, 0.0, 0.360784313725, -0.21600000000000008, 0.0, 1.0, 1.0, 0.1295999999999996, 0.0, 0.501960784314, 0.0, 0.4703999999999998, 1.0, 1.0, 0.0, 0.8135999999999998, 1.0, 0.380392156863, 0.0, 1.1568000000000005, 0.419607843137, 0.0, 0.0, 1.5, 0.878431372549, 0.301960784314, 0.301960784314]
cpLUT.ColorSpace = 'RGB'
cpLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Cp'
cpPWF = GetOpacityTransferFunction('Cp')
cpPWF.Points = [-0.9, 0.0, 0.5, 0.0, 1.5, 1.0, 0.5, 0.0]
cpPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
cp300Display.Representation = 'Surface'
cp300Display.ColorArrayName = ['POINTS', 'Cp']
cp300Display.LookupTable = cpLUT
cp300Display.SelectTCoordArray = 'None'
cp300Display.SelectNormalArray = 'None'
cp300Display.SelectTangentArray = 'None'
cp300Display.OSPRayScaleArray = 'Cp'
cp300Display.OSPRayScaleFunction = 'PiecewiseFunction'
cp300Display.SelectOrientationVectors = 'U'
cp300Display.ScaleFactor = 0.15000000000000002
cp300Display.SelectScaleArray = 'Cp'
cp300Display.GlyphType = 'Arrow'
cp300Display.GlyphTableIndexArray = 'Cp'
cp300Display.GaussianRadius = 0.0075
cp300Display.SetScaleArray = ['POINTS', 'Cp']
cp300Display.ScaleTransferFunction = 'PiecewiseFunction'
cp300Display.OpacityArray = ['POINTS', 'Cp']
cp300Display.OpacityTransferFunction = 'PiecewiseFunction'
cp300Display.DataAxesGrid = 'GridAxesRepresentation'
cp300Display.PolarAxes = 'PolarAxesRepresentation'
cp300Display.ScalarOpacityFunction = cpPWF
cp300Display.ScalarOpacityUnitDistance = 0.07071146378845614
cp300Display.OpacityArrayName = ['POINTS', 'Cp']
cp300Display.SelectInputVectors = ['POINTS', 'U']
cp300Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cp300Display.ScaleTransferFunction.Points = [-1.3332616215870703, 0.0, 0.5, 0.0, 1.181561932795579, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cp300Display.OpacityTransferFunction.Points = [-1.3332616215870703, 0.0, 0.5, 0.0, 1.181561932795579, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for cpLUT in view renderView1
cpLUTColorBar = GetScalarBar(cpLUT, renderView1)
cpLUTColorBar.Title = 'Cp'
cpLUTColorBar.ComponentTitle = ''

# set color bar visibility
cpLUTColorBar.Visibility = 1

# show color legend
cp300Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(cp300)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')