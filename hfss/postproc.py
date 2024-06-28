oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("plot",
                     "Modal Solution Data",
                     "Rectangular Plot",
                     "setup : main_sweep", 
                     ["Domain:=", "Sweep"],
                     ["Freq:=", ["All"]], 
                     ["X Component:=", "Freq",
                      "Y Component:=", ["dB(S(1,1))", "db(S(1,2))", "db(S(1, 3))", "db(S(1,4))"]], [])
oModule.ExportToFile("plot", "generated.csv")
