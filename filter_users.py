import json

def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)

def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(f"{user["name"]}: {user["age"]}, ID:{user["id"]}, {user["email"]}")

def filter_by_mail(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(f"{user["name"]}: {user["email"]}, ID:{user["id"]}, {user["age"]}")

if __name__ == "__main__":
    filter_option = input(f"What would you like to filter by?\n(Currently, only 'name'(1), 'age'(2) and 'email'(3) is supported): ").strip().lower()
    
    if filter_option == "name" or filter_option == "1":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age" or filter_option == "2":
        while True:
            try:
                age_to_search = int(input("Enter a age to filter users: "))
                if age_to_search >= 0:
                    filter_users_by_age(age_to_search)
                    break
            except ValueError:
                print("Only numbers are allowed here")
    elif filter_option == "email" or filter_option =="3":
        mail_to_search = input("Enter a mail to filter users: ")
    else:
        print("Filtering by that option is not yet supported.")
