-- app = pf.GetApplication()
-- app:OpenFile("39_stacked_patch_from_ieee_paper_s_band.fek")
names = pf.Excitation.GetNames()
dataset = pf.Excitation.GetDataSet(names[1])
frequency_axis = dataset.Axes["Frequency"]
print("--START--")
for i = 1,#frequency_axis do
    z = dataset[i].Impedance
    znorm = z/50
    s11 = (znorm-1)/(znorm+1)
    freq = frequency_axis[i]
    print(string.format("%f, %f", freq, 20*math.log10(s11:Abs())));
end
print("--END--")