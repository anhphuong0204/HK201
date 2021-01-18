a = "\"Get rid of this please\""
b = "Get this\\h to"

if (a.find("\"") != -1):
    a = a[1:-1]
k = b.find("\\")
b = b[0:(k+2)]


print(a)
print("\n")
print(b)
