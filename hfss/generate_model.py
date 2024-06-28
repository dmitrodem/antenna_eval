if True:
    oProject = oDesktop.NewProject()
    oProject.InsertDesign("HFSS", "design", "DrivenModal", "")
else:
    oProject = oDesktop.GetActiveProject()

oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")
oDefinitionManager = oProject.GetDefinitionManager()

oDefinitionManager.EditMaterial("Rogers RO4003 (tm)",
                                ["NAME:Rogers RO4003 (tm)",
                                 "CoordinateSystemType:=", "Cartesian",
                                 ["NAME:AttachedData"],
                                 ["NAME:ModifierData"],
                                 "permittivity:=", "3.38",
                                 "dielectric_loss_tangent:=", "0.0027"])

def import_step(name, index):
    oEditor.Import(["NAME:NativeBodyParameters",
                    "SourceFile:=", "../cad/{0}.step".format(name)])
    oEditor.RenamePart(["NAME:Rename Data",
                        "Old Name:=", oEditor.GetObjectName(index),
                        "New Name:=", name])
    oEditor.DuplicateMirror(["NAME:Selections",
                             "Selections:=", name],
                            ["NAME:DuplicateToMirrorParameters", 
                             "DuplicateMirrorBaseX:=", "0mm",
                             "DuplicateMirrorBaseY:=", "0mm",
                             "DuplicateMirrorBaseZ:=", "0mm",
                             "DuplicateMirrorNormalX:=", "0mm",
                             "DuplicateMirrorNormalY:=", "1mm",
                             "DuplicateMirrorNormalZ:=", "0mm"],
                            ["NAME:Options",
                             "DuplicateBoundaries:=", False])
    oEditor.Unite(["NAME:Selections",
                   "Selections:=", ",".join([name, "{0}_1".format(name)])],
                  ["NAME:UniteParameters",
                   "KeepOriginals:=", False])

import_step("01_splitter",    0)
import_step("02_feedline",    1)
import_step("03_combined",    2)
import_step("04_slots",       3)
import_step("05_small_patch", 4)
import_step("06_large_patch", 5)

oEditor.CreateRectangle(["NAME:RectangleParameters",
                         "IsCovered:=", True,
                         "XStart:=", "-50mm",
                         "YStart:=", "-50mm",
                         "ZStart:=", "0mm",
                         "Width:=", "100mm",
                         "Height:=", "100mm",
                         "WhichAxis:=", "Z"],
                        ["NAME:Attributes",
                         "Name:=", "07_gnd",
                         "PartCoordinateSystem:=", "Global"])

oEditor.Subtract(["NAME:Selections",
                  "Blank Parts:=", "07_gnd",
                  "Tool Parts:=", "04_slots"],
                 ["NAME:SubtractParameters",
                  "KeepOriginals:="	, False])

oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["01_splitter", "02_feedline", "03_combined"])], 
             ["NAME:TranslateParameters",
              "TranslateVectorZ:=", "-0.508mm"])

oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["05_small_patch", "06_large_patch"])], 
             ["NAME:TranslateParameters",
              "TranslateVectorZ:=", "1.524mm"])

oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["06_large_patch"])], 
             ["NAME:TranslateParameters",
              "TranslateVectorZ:=", "9mm"])

oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["06_large_patch"])], 
             ["NAME:TranslateParameters",
              "TranslateVectorZ:=", "1.524mm"])

oEditor.CreateRectangle(["NAME:RectangleParameters",
                         "IsCovered:=", True,
                         "XStart:=", "-50mm",
                         "YStart:=", "-50mm",
                         "ZStart:=", "0mm",
                         "Width:=", "100mm",
                         "Height:=", "100mm",
                         "WhichAxis:=", "Z"],
                        ["NAME:Attributes",
                         "Name:=", "08_feed_substrate",
                         "PartCoordinateSystem:=", "Global"])

oEditor.SweepAlongVector(["NAME:Selections",
                          "Selections:=", "08_feed_substrate"], 
                         ["NAME:VectorSweepParameters",
                          "SweepVectorZ:="	, "-0.508mm"])

oEditor.CreateRectangle(["NAME:RectangleParameters",
                         "IsCovered:=", True,
                         "XStart:=", "-50mm",
                         "YStart:=", "-50mm",
                         "ZStart:=", "0mm",
                         "Width:=", "100mm",
                         "Height:=", "100mm",
                         "WhichAxis:=", "Z"],
                        ["NAME:Attributes",
                         "Name:=", "09_small_patch_substrate",
                         "PartCoordinateSystem:=", "Global"])

oEditor.SweepAlongVector(["NAME:Selections",
                          "Selections:=", "09_small_patch_substrate"], 
                         ["NAME:VectorSweepParameters",
                          "SweepVectorZ:="	, "1.524mm"])

oEditor.CreateRectangle(["NAME:RectangleParameters",
                         "IsCovered:=", True,
                         "XStart:=", "-55mm/2",
                         "YStart:=", "-55mm/2",
                         "ZStart:=", "0mm",
                         "Width:=", "55mm",
                         "Height:=", "55mm",
                         "WhichAxis:=", "Z"],
                        ["NAME:Attributes",
                         "Name:=", "10_large_patch_substrate",
                         "PartCoordinateSystem:=", "Global"])

oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["10_large_patch_substrate"])], 
             ["NAME:TranslateParameters",
              "TranslateVectorZ:=", "1.524mm+9mm"])

oEditor.SweepAlongVector(["NAME:Selections",
                          "Selections:=", "10_large_patch_substrate"], 
                         ["NAME:VectorSweepParameters",
                          "SweepVectorZ:="	, "1.524mm"])

oEditor.AssignMaterial(["NAME:Selections",
                        "Selections:=", ",".join(["08_feed_substrate", "09_small_patch_substrate", "10_large_patch_substrate"])], 
                       ["NAME:Attributes",
                        "MaterialValue:=", "\"Rogers RO4003 (tm)\"",
                        "SolveInside:=", True])

#### Port
oEditor.CreateRectangle(["NAME:RectangleParameters",
                         "IsCovered:=", True,
                         "XStart:=", "0mm",
                         "YStart:=", "-0.5mm",
                         "ZStart:=", "0mm",
                         "Width:=", "0.508mm",
                         "Height:=", "1mm",
                         "WhichAxis:=", "Z"], 
                        ["NAME:Attributes",
                         "Name:=", "11_port1",
                         "PartCoordinateSystem:=", "Global"])
oEditor.Rotate(["NAME:Selections",
                "Selections:=", ",".join(["11_port1"])],
               ["NAME:RotateParameters",
                "RotateAxis:=", "Y",
                "RotateAngle:=", "90deg"])
oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["11_port1"])],
             [
                 "NAME:TranslateParameters",
                 "TranslateVectorX:=", "50mm",
                 "TranslateVectorY:=", "25mm",
                 "TranslateVectorZ:=", "0mm"])

oEditor.CreateRectangle(["NAME:RectangleParameters",
                         "IsCovered:=", True,
                         "XStart:=", "0mm",
                         "YStart:=", "-0.5mm",
                         "ZStart:=", "0mm",
                         "Width:=", "0.508mm",
                         "Height:=", "1mm",
                         "WhichAxis:=", "Z"], 
                        ["NAME:Attributes",
                         "Name:=", "12_port2",
                         "PartCoordinateSystem:=", "Global"])
oEditor.Rotate(["NAME:Selections",
                "Selections:=", ",".join(["12_port2"])],
               ["NAME:RotateParameters",
                "RotateAxis:=", "Y",
                "RotateAngle:=", "90deg"])
oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["12_port2"])],
             [
                 "NAME:TranslateParameters",
                 "TranslateVectorX:=", "50mm",
                 "TranslateVectorY:=", "-25mm",
                 "TranslateVectorZ:=", "0mm"])

oEditor.CreateRectangle(["NAME:RectangleParameters",
                         "IsCovered:=", True,
                         "XStart:=", "0mm",
                         "YStart:=", "-0.5mm",
                         "ZStart:=", "0mm",
                         "Width:=", "0.508mm",
                         "Height:=", "1mm",
                         "WhichAxis:=", "Z"], 
                        ["NAME:Attributes",
                         "Name:=", "13_port3",
                         "PartCoordinateSystem:=", "Global"])
oEditor.Rotate(["NAME:Selections",
                "Selections:=", ",".join(["13_port3"])],
               ["NAME:RotateParameters",
                "RotateAxis:=", "Y",
                "RotateAngle:=", "90deg"])
oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["13_port3"])],
             [
                 "NAME:TranslateParameters",
                 "TranslateVectorX:=", "-50mm",
                 "TranslateVectorY:=", "-25mm",
                 "TranslateVectorZ:=", "0mm"])

oEditor.CreateRectangle(["NAME:RectangleParameters",
                         "IsCovered:=", True,
                         "XStart:=", "0mm",
                         "YStart:=", "-0.5mm",
                         "ZStart:=", "0mm",
                         "Width:=", "0.508mm",
                         "Height:=", "1mm",
                         "WhichAxis:=", "Z"], 
                        ["NAME:Attributes",
                         "Name:=", "14_port4",
                         "PartCoordinateSystem:=", "Global"])
oEditor.Rotate(["NAME:Selections",
                "Selections:=", ",".join(["14_port4"])],
               ["NAME:RotateParameters",
                "RotateAxis:=", "Y",
                "RotateAngle:=", "90deg"])
oEditor.Move(["NAME:Selections",
              "Selections:=", ",".join(["14_port4"])],
             [
                 "NAME:TranslateParameters",
                 "TranslateVectorX:=", "-50mm",
                 "TranslateVectorY:=", "25mm",
                 "TranslateVectorZ:=", "0mm"])

oEditor.CreateBox(["NAME:BoxParameters",
                   "XPosition:=", "-100mm",
                   "YPosition:=", "-100mm",
                   "ZPosition:=", "-50mm",
                   "XSize:=", "200mm",
                   "YSize:=", "200mm",
                   "ZSize:=", "150mm"], 
                  ["NAME:Attributes",
                   "Name:=", "15_airbox",
                   "MaterialValue:=", "\"vacuum\"",
                   "SolveInside:=", True,
                   "PartCoordinateSystem:=", "Global"])

### Conditions

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignPerfectE(["NAME:GND",
                        "Objects:=", ["07_gnd"],
                        "InfGroundPlane:="	, False])
oModule.AssignPerfectE(["NAME:01_splitter",
                        "Objects:=", ["01_splitter"],
                        "InfGroundPlane:="	, False])
oModule.AssignPerfectE(["NAME:02_feedline",
                        "Objects:=", ["02_feedline"],
                        "InfGroundPlane:="	, False])
oModule.AssignPerfectE(["NAME:03_combined",
                        "Objects:=", ["03_combined"],
                        "InfGroundPlane:="	, False])
oModule.AssignPerfectE(["NAME:05_small_patch",
                        "Objects:=", ["05_small_patch"],
                        "InfGroundPlane:="	, False])
oModule.AssignPerfectE(["NAME:06_large_patch",
                        "Objects:=", ["06_large_patch"],
                        "InfGroundPlane:="	, False])
oModule.AssignLumpedPort(["NAME:1",
                          "Objects:=", ["11_port1"],
                          "RenormalizeAllTerminals:=", True,
                          "DoDeembed:="		, False,
                          ["NAME:Modes", ["NAME:Mode1",
                                          "ModeNum:=", 1,
                                          "UseIntLine:=", True,
                                          ["NAME:IntLine",
                                           "Start:=", ["50mm","25mm","-0.508mm"],
                                           "End:=", ["50mm","25mm","0mm"]],
                                          "CharImp:=", "Zpi",
                                          "AlignmentGroup:=", 0,
                                          "RenormImp:=", "50ohm"]],
                          "ShowReporterFilter:=", False,
                          "ReporterFilter:=", [True],
                          "FullResistance:=", "50ohm",
                          "FullReactance:=", "0ohm"])
oModule.AssignLumpedPort(["NAME:2",
                          "Objects:=", ["12_port2"],
                          "RenormalizeAllTerminals:=", True,
                          "DoDeembed:="		, False,
                          ["NAME:Modes", ["NAME:Mode1",
                                          "ModeNum:=", 1,
                                          "UseIntLine:=", True,
                                          ["NAME:IntLine",
                                           "Start:=", ["50mm","-25mm","-0.508mm"],
                                           "End:=", ["50mm","-25mm","0mm"]],
                                          "CharImp:=", "Zpi",
                                          "AlignmentGroup:=", 0,
                                          "RenormImp:=", "50ohm"]],
                          "ShowReporterFilter:=", False,
                          "ReporterFilter:=", [True],
                          "FullResistance:=", "50ohm",
                          "FullReactance:=", "0ohm"])
oModule.AssignLumpedPort(["NAME:3",
                          "Objects:=", ["13_port3"],
                          "RenormalizeAllTerminals:=", True,
                          "DoDeembed:="		, False,
                          ["NAME:Modes", ["NAME:Mode1",
                                          "ModeNum:=", 1,
                                          "UseIntLine:=", True,
                                          ["NAME:IntLine",
                                           "Start:=", ["-50mm","-25mm","-0.508mm"],
                                           "End:=", ["-50mm","-25mm","0mm"]],
                                          "CharImp:=", "Zpi",
                                          "AlignmentGroup:=", 0,
                                          "RenormImp:=", "50ohm"]],
                          "ShowReporterFilter:=", False,
                          "ReporterFilter:=", [True],
                          "FullResistance:=", "50ohm",
                          "FullReactance:=", "0ohm"])
oModule.AssignLumpedPort(["NAME:4",
                          "Objects:=", ["14_port4"],
                          "RenormalizeAllTerminals:=", True,
                          "DoDeembed:="		, False,
                          ["NAME:Modes", ["NAME:Mode1",
                                          "ModeNum:=", 1,
                                          "UseIntLine:=", True,
                                          ["NAME:IntLine",
                                           "Start:=", ["-50mm","25mm","-0.508mm"],
                                           "End:=", ["-50mm","25mm","0mm"]],
                                          "CharImp:=", "Zpi",
                                          "AlignmentGroup:=", 0,
                                          "RenormImp:=", "50ohm"]],
                          "ShowReporterFilter:=", False,
                          "ReporterFilter:=", [True],
                          "FullResistance:=", "50ohm",
                          "FullReactance:=", "0ohm"])

oModule.AssignRadiation(["NAME:radiation",
                         "Objects:=", ["15_airbox"],
                         "IsIncidentField:=", False,
                         "IsEnforcedHField:=", False,
                         "IsEnforcedEField:=", False,
                         "IsFssReference:=", False,
                         "IsForPML:=", False,
                         "UseAdaptiveIE:=", False,
                         "IncludeInPostproc:=", True])


## Final setup
oEditor.ChangeProperty(["NAME:AllTabs",	
                        ["NAME:Geometry3DCmdTab",
                         ["NAME:PropServers", "07_gnd:Subtract:1"],
                         ["NAME:ChangedProps", 
                          ["NAME:Suppress Command",
                           "Value:=", True]]]])
oEditor.ChangeProperty(["NAME:AllTabs",
                        ["NAME:Geometry3DAttributeTab",
                         ["NAME:PropServers", "02_feedline"],
                         ["NAME:ChangedProps",
                          ["NAME:Model", "Value:=", False]]]])
oEditor.ChangeProperty(["NAME:AllTabs",
                        ["NAME:Geometry3DAttributeTab",
                         ["NAME:PropServers", "03_combined"],
                         ["NAME:ChangedProps",
                          ["NAME:Model", "Value:=", False]]]])

## Solution setup
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven",
                    ["NAME:setup",
                     "Frequency:=", "2.1GHz",
                     "MaxDeltaS:=", 0.01,
                     "MaximumPasses:=", 10,
                     "MinimumPasses:=", 1,
                     "MinimumConvergedPasses:=", 1])

oModule.InsertFrequencySweep("setup",
                             ["NAME:main_sweep",
                              "IsEnabled:=", True,
                              "SetupType:=", "LinearStep",
                              "StartValue:=", "1.8GHz",
                              "StopValue:=", "2.4GHz",
                              "StepSize:=", "0.01GHz",
                              "Type:=", "Interpolating",
                              "SaveFields:=", False,
                              "SaveRadFields:=", False,
                              "InterpTolerance:=", 0.5,
                              "InterpMaxSolns:=", 250,
                              "InterpMinSolns:=", 0,
                              "InterpMinSubranges:=", 1,
                              "ExtrapToDC:=", False,
                              "InterpUseS:=", True,
                              "InterpUsePortImped:=", False,
                              "InterpUsePropConst:=", True,
                              "UseDerivativeConvergence:=", False,
                              "InterpDerivTolerance:=", 0.2,
                              "UseFullBasis:=", True,
                              "EnforcePassivity:=", True,
                              "PassivityErrorTolerance:=", 0.0001])

## Save project
oProject.SaveAs("generated.hfss", True)
