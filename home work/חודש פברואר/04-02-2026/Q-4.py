
while True:
    last_name = input("Enter your last name with upper-case letters: ")
    if last_name.isupper():
        break
    print("try again")

while True:
    first_name = input("Enter your first name with lower-case letters: ")
    if first_name.islower():
        break
    print("try again")
while True:
    country_name = input("your country length name must be at most 3 letters: ")
    if len(country_name) < 4 and country_name.isalpha():
        break
    print("try again")
while True:
    zip_code: str = (input("Enter your zip code: "))

    if zip_code.isdigit() and len(zip_code) >= 4:


        break
    print("try again")
city_name : str = input("Enter your city address: ")
print("*" * 50)
print(f'''FOR: {last_name}, {first_name}
COUNTRY: {country_name}
ADDRESS: {city_name}
ZIPCODE: {zip_code}''')

