numrat = {
    "KS" : "+383",
    "IT" : "+39",
    "AL" : "+355"
}

kosova = numrat["KS"]

print(kosova)

numrat ["KS"] = "+377"
print(numrat["KS"])


del numrat["AL"]

print(numrat)


keys = numrat.keys()
vlerat = numrat.values()
print(keys)
print(vlerat)