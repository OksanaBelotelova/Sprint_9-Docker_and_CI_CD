import random
import string

class RandomUserData:

    def random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    def generate_email(self):
        user = RandomUserData
        name = user.random_string(self, 7)
        email = f'{name}@mail.com'
        return email