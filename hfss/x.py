# ----------------------------------------------
# Script Recorded by Ansoft HFSS Version 2014.0.0
# 16:04:25  Jun 21, 2024
# ----------------------------------------------
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("07_tune_s_band")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWavePort(
	[
		"NAME:2",
		"Objects:="		, ["port2"],
		"NumModes:="		, 1,
		"RenormalizeAllTerminals:=", True,
		"UseLineModeAlignment:=", False,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["0mm","50mm","0mm"],
					"End:="			, ["0mm","50mm","-0.508mm"]
				],
				"CharImp:="		, "Zpi",
				"AlignmentGroup:="	, 0
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"UseAnalyticAlignment:=", False
	])
