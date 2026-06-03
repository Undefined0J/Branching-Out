"""
Script to load user data from a JSON file and filter it based on user input.
"""

import json


def load_users(file_path: str) -> list:
    """
    Load user data from a specified JSON file.

    :param file_path: The path to the JSON file.
    :return: A list of dictionaries containing user data, or an empty list if an error occurs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return []


def filter_users_by_name(users: list, name: str) -> list:
    """
    Filter a list of users by their name.

    :param users: List of user dictionaries.
    :param name: The name to search for (case-insensitive).
    :return: A list of user dictionaries that match the given name.
    """
    # Return users where the name matches the search string
    return [user for user in users if user.get("name", "").lower() == name.lower()]


def filter_users_by_age(users: list, age: int) -> list:
    """
    Filter a list of users by their age.

    :param users: List of user dictionaries.
    :param age: The exact age to search for.
    :return: A list of user dictionaries that match the given age.
    """
    return [user for user in users if user.get("age") == age]


def display_users(users: list) -> None:
    """
    Print the details of each user in the provided list.

    :param users: List of user dictionaries.
    """
    if not users:
        print("No users found matching the criteria.")
        return

    # Iterate and print each user record
    for user in users:
        print(user)


def main() -> None:
    """
    Main execution flow: load data, prompt user for filter criteria, and display results.
    """
    file_name = "users.json"
    users_data = load_users(file_name)

    # Prompt for filter option
    filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filtered_users = filter_users_by_name(users_data, name_to_search)
        display_users(filtered_users)

    elif filter_option == "age":
        age_input = input("Enter an age to filter users: ").strip()
        try:
            # Safely convert input to integer
            age_to_search = int(age_input)
            filtered_users = filter_users_by_age(users_data, age_to_search)
            display_users(filtered_users)
        except ValueError:
            print("Error: Age must be a valid number.")

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()