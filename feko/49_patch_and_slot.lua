print("--START--")
name = pf.NearField.GetNames()[1];
dataset = pf.NearField.GetDataSet(name);
frequency = dataset.Axes["Frequency"];
for i = 1,#frequency do
    Hy = dataset[i][1][1][1].HFieldComp2;
    freq = frequency[i];
    print(string.format("%.6f, %.6f", freq, Hy.re^2 + Hy.im^2));
end
print("--END--")