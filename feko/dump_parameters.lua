app = cf.GetApplication()
project = app.Project
vars = project.Variables
for i = 1,#vars do
    v = vars[i]
    --print(string.format("%s, \"%s\", %.6f, \"%s\"", 
    --    v.Name, v.Expression, v.Value, v.Description));
    print(string.format("\"%s\" : %.6f,", v.Name, v.Value));
end
