
        
app = pf.GetApplication()
far_field_data = app.Models[1].Configurations[1].FarFields[1]
dset = far_field_data:GetDataSet()
inspect(dset)
for i = 1,#dset.Axes["Frequency"] do
for j = 1,#dset.Axes["Theta"] do
    for k = 1,#dset.Axes["Phi"] do
        print(dset[i][j][k]["DirectivityFactor"])
    end
end
end
