string = "adarsh gupta"
for x in string[:].split():
    string = string.replace(x,x.capitalize())
print(string)