#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment2B

#welcome menu
print("[Loan Approval System]")

#user input
age = int(input("Enter your age: "))
income = int(input("Enter your income: $"))
creditscore = int(input("Enter your credit score: "))

#credit score validation
if creditscore < 300 or creditscore > 850:
        print("Invalid credit score. Score must be between 300 and 850.")
        exit()

#age validation
else:
    if age < 18:
        print("You do not qualify for a loan due to age.")
        exit()

#credit score match case

match creditscore:
    case creditscore if 700 <= creditscore <= 850:
        creditscore = "Good"
    case creditscore if 600 <= creditscore <= 699:
        creditscore = "Fair"
    case creditscore if 300 <= creditscore <= 599:
        creditscore = "Poor"

#automatic denial
if creditscore == "Poor":
    print("You do not qualify for a loan due to poor credit.")
#income to credit score match case and approval
else:
    if income >=100_000 and creditscore == "Good":
        print("You qualify for a Premium Loan.")
    elif income >= 50_000 < 100_000:
        if creditscore == "Good" or creditscore == "Fair":
            print("You qualify for a Standard Loan")
    elif income < 50_000 and creditscore == "Fair":
        print("You qualify for a Basic Loan.")
    else:
        print("Your income is too low for a loan")

