"""Script for load users of prove"""

# Utilities
import random
import csv


class User:
    """Create users class"""
    def __init__(self, how_many_users):
        self.how_many_users = how_many_users

    @staticmethod
    def phone_number(self):
        """Create phone number random"""
        phone_number = []
        for i in range(10):
            num = str(random.randint(3, 9))
            phone_number.append(num)
        phone_num = ''.join(phone_number)
        return phone_num

    @staticmethod
    def create_names(self):
        """Create names random with names in list of names base"""
        firsts_names = ['Maria', 'Ricardina', 'Mario', 'Lola', 'Sasha', 'Esteban', 'Martin', 'Juan']
        lasts_names = ['Rodriguez', 'Hernandez', 'Aristizabal', 'Montolivo']

        first_name = random.choice(firsts_names)
        last_name = random.choice(lasts_names)

        return [first_name, last_name]

    @staticmethod
    def password(self):
        """Create random password """
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        big_letters = list(LETTERS)
        small_letters = list((LETTERS).lower())
        numbers = list('123456789')
        password = []
        for i in range(random.randint(3, 5)):
            password.append(random.choice(big_letters))
            password.append(random.choice(small_letters))
            password.append(random.choice(numbers))
        random.shuffle(password)
        password = ''.join(password)
        return password

    def write_user(self):
        """Write users in csv file"""
        with open('users.csv', 'w') as users_file:
            writer = csv.writer(users_file)
            writer.writerow(['phone', 'first_name', 'last_name', 'password ', 'email'])
            for i in range(self.how_many_users):
                phone_number = self.phone_number()
                names = self.create_names()
                first_name = names[0]
                last_name = names[1]
                password = self.password()
                email = names[0].lower() + names[1].lower() + '@email.com'
                writer.writerow([
                    phone_number,
                    first_name,
                    last_name,
                    password,
                    email
                ])


def run():
    """Get input, number of users to create and run logic to create users."""

    how_many_users = int(input('¿Cuantos usuarios quiere crear?: '))
    create_user = User(how_many_users).write_user
    create_user()
    print(f'Se ha creado {how_many_users} usuarios')


if __name__ == '__main__':
    run()
