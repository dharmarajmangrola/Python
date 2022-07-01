#Accept the height of a person & categorize as taller, dwarf & average.

height = float(input("Enter the person height :- "))

if height > 175.4:
    print("taller")

elif height > 147:
    print("dwarf")

else:
    print("average")