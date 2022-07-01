#Dharmaraj scored 45 in Mathematics, 38 in Gujarati, 30 in Social Science, 42 in English and 39 in Science. Now calculate sum of five subject's marks anf=d find percentage. maximum marks in one subject is 100.

Mathematics = float(input("Enter Mathematics Score :- "))
Gujarati = float(input("Enter Gujarati Score :- "))
Socialscience = float(input("Enter Social Science Score :-"))
English = float(input("Enter English Score :-"))
Science = float(input("Enter Science Score :-"))

Total = Mathematics + Gujarati + Socialscience + English + Science
average = Total/5
percentage = (Total/500)*100

print("Total marks = ",Total)
print("Average marks = ", average)
print("student final percentage = ",percentage)