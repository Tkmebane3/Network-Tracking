
def data_log():
    with open("Database.txt", "a") as file:
        database = {}
        name = input("Who did you meet today? ").strip()
        event = input(f"Where did you meet {name}? ")
        occupation = input(f"What does {name} do for work? ")
        interests = input(f"What similar interests did you share with {name}? ")

        database[name] = {
            "event" : event,
            "occupation" : occupation,
            "interests" : interests
            }

        entry = f"{name} - Met at: {event} | Job: {occupation} | Shared interests: {interests}\n"
        file.write(entry)

        print(f"{name}'s information successfuly saved!\n")

def main():
    print("Your current network:\n")
    while True:
        try:
            with open("Database.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    for i, line in enumerate(lines, 1):
                        print(f"{i}.{line.strip()}\n")
                else:
                    print("No contacts logged yet.")
        except FileNotFoundError:
            print("No contacts on file.")
        add_con = input("\nWould you like to add a contact?\n")
        if add_con.lower() != "yes":
            print("Goodbye!")
            break
        else:
            data_log()
main()
        
            
