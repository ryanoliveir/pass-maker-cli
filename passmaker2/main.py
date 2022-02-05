from passmaker import Passmaker



print("pmaker > Number of characters:",)
numChar = int(input("=> "))

print("pmaker > Number of passwords ",)
numPass = int(input("=> "))




pmaker = Passmaker(numChar, numPass, "all")
pmaker.set_passConfig()



print(*pmaker.construct(), sep="\n")