
CURRENT_YEAR=2025                        #присвоил значение текущего года в конcтанту


"""определил функцию, которая вычисляет стадию жизни человека"""
def generate_profile(current_age):
    if 0<=current_age<=12:
        return "Child"
    if 13<=current_age<=19:
        return "Teenager"
    if current_age>=20:
        return "Adult"


"""обернул все основную логику приложения в одноименную функцию для удобства вызова и читаемости"""
def main():
    print("Wasuuuup! Actually i mean hello, friend")
    user_name=input("Enter your full name: ")
    birth_year_str=input("Enter your birth year: ")
    birth_year=int(birth_year_str)
    current_age=CURRENT_YEAR-birth_year
    hobbies=[]
    """бесконечный цикл с остановкой, при слове опрашивающий хобби"""
    while True:
        entry_hobby=input("Enter a favorite hobby or type 'stop' to finish: ")
        if entry_hobby.lower()=="stop":
            break
        else:
            hobbies.append(entry_hobby)

    life_stage=generate_profile(current_age)        #присвоил вернуввшийся результат вычисления функций в переменную
    user_profile={
    "name" : user_name,
    "age" : current_age,
    "life_stage" : life_stage,
    "hobbies" : hobbies
    }
    """процесс вывода и минимальная логика с проверкой на пустоту списка"""
    print("---")
    print("Profile Summary: ")
    print(f"Name: {user_name.title()}")
    print(f"Age: {current_age}")
    print(f"Life Stage: {life_stage}")
    if not hobbies:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(hobbies)}): ")
        for hobby in hobbies:
            print(f"- {hobby.title()}")
    print("---")

if __name__ == "__main__":          #проверка на корректность вызова функции мейн
    main()


