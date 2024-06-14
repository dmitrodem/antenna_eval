name = pf.Excitation.GetNames()[1];
dataset = pf.Excitation.GetDataSet(name);
frequency = dataset.Axes["Frequency"];
print("--START--")
for i = 1,#frequency do
    Z = dataset[i]["Impedance"];
    freq = frequency[i];
    print(string.format("%.6f, %.6f, %.6f", freq, Z.re, Z.im));
end
print("--END--")
