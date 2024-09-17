def user(name, age, location):
    return f'Hello {name}, you are {age} years old and live in {location}.'

name=input('Enter name here:\n')
age=input('Enter age:\n')
location=input('Enter location here:\n')

print(user(name, age, location));