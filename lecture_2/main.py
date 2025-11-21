CURRENT_YEAR = 2025  # fixed current year used to calculate the user's age


def generate_profile(current_age: int) -> str:
    """
    return the user's life stage based on their age.
    """
    if 0 <= current_age <= 12:
        return "Child"
    elif 13 <= current_age <= 19:
        return "Teenager"
    else:
        return "Adult"


def main() -> None:
    """main function that runs the mini profile generator."""
    print("Wasuuuup! Actually I mean hello, friend")

    # basic user info
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_age = CURRENT_YEAR - birth_year

    # collect hobbies from the user until they choose to stop
    hobbies: list[str] = []
    while True:
        entry_hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if entry_hobby.lower() == "stop":
            break
        hobbies.append(entry_hobby)

    # determine the user's life stage using the helper function
    life_stage = generate_profile(current_age)

    # bundle all collected user data into a single dictionary
    user_profile = {
        "name": user_name,
        "age": current_age,
        "life_stage": life_stage,
        "hobbies": hobbies,
    }

    # nicely formatted profile summary
    print("---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name'].title()}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['life_stage']}")

    # check if the user listed any hobbies
    if not user_profile["hobbies"]:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile["hobbies"]:
            print(f"- {hobby.title()}")

    print("---")


# run main only when this file is executed directly, not when imported
if __name__ == "__main__":
    main()