#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab8A

email_list = []


def main():
    print("[Mailing List]")

    while True:
        print("\n1 - Add email"
              "\n2 - Delete email"
              "\n3 - List all emails"
              "\n4 - Quit")

        user_input = int(input("Make your selection: "))

        match user_input:

            case 1:
                email = input("\nEnter the email to be added: ")
                email_list.append(email)
                print(f"{email} was added to the mailing list.")

            case 2:
                del_email = input("Enter the email to be deleted: ")
                if del_email in email_list:
                    email_list.remove(del_email)
                    print(f"{del_email} has been removed from the mailing list")
                else:
                    print(f"No such email in mailing list: {del_email}")
            case 3:
                print()
                for x in email_list:
                    print(x)
            case 4:
                print()
                print("Shutting down...")
                break



if __name__ == "__main__":
    main()