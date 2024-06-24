# ----------------------------------------------
# Script Recorded by Ansoft HFSS Version 2014.0.0
# 17:03:45  Jun 14, 2024
# ----------------------------------------------
variables = {
        "H_a" : 9.000000,
        "H_s1" : 0.508000,
        "H_s2" : 1.524000,
        "H_s3" : 1.524000,
        "L_s1" : 8.700000,
        "L_s2" : 5.000000,
        "L_stub1" : 3.600000,
        "L_stub2" : 2.600000,
        "L_stub3" : 15.000000,
        "W_ms" : 1.150000,
        "W_p1" : 36.000000,
        "W_p2" : 48.500000,
        "W_s1" : 0.800000,
        "W_s2" : 4.500000,
        "offset" : 14.500000,
        "offset_h" : 0.300000,
        "ustrip_l" : 35.000000,
        "ustrip_stub" : 3.250000,
}
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()

for k in variables.keys():
    print("{0} {1}".format(k, variables[k]))
    oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:LocalVariableTab",
                [
                    "NAME:PropServers", 
                    "LocalVariables"
                ],
                [
                    "NAME:NewProps",
                    [
                        "NAME:{0}".format(k),
                        "PropType:="		, "VariableProp",
                        "UserDef:="		, True,
                        "Value:="		, "{0}mm".format(variables[k])
                    ]
                ]
            ]
        ])
