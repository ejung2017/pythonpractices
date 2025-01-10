import random, datetime 


def generateBirthday(): 

    while True: 
        numberOfDays = 0
        numberOfDays = input("How many days of birthdays do you want to generate? \n")
        birthdays = []
        for i in range(int(numberOfDays)): 
            start_date = datetime.date(2001, 1, 1)
            days = random.randint(0, 364)
            birthday = start_date + datetime.timedelta(days=days)
            birthday = birthday.strftime("%b %d")
            birthdays.append(birthday)
        break
    return ', '.join(birthdays)

#simulating birthdays to check how many people share the same birthday


birthday = generateBirthday()
print(birthday)