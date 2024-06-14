names = pf.SParameter.GetNames()
sParam = pf.SParameter.GetDataSet(names[1])
frequency_axis = sParam.Axes["Frequency"]
print("--START--")
for i = 1,16 do
	smn = sParam[1][i]["SParameter"]
	print(string.format("%f, %f", smn.re, smn.im));
end
print("--END--")
