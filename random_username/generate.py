import os
import random


class UsernameGenerator(object):
    _instance = None
    _adjectives = []
    _nouns = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UsernameGenerator, cls).__new__(cls)
            directory_path = os.path.dirname(__file__)
            with open(os.path.join(directory_path, 'data', 'adjectives.txt'), 'r') as file_adjective:
                with open(os.path.join(directory_path, 'data', 'nouns.txt'), 'r') as file_noun:
                    for line in file_adjective:
                        cls._adjectives.append(line.strip())
                    for line in file_noun:
                        cls._nouns.append(line.strip())
        return cls._instance

    def generate_username(self, num_digits=1, *args, **kwargs):
        if num_digits < 1:
            raise ValueError("num_digits should be greater than 0")
        adjective = random.choice(self._adjectives)
        noun = random.choice(self._nouns).capitalize()
        number = int(
            random.random()
            * (10**num_digits)
        )
        return adjective + noun + str(number)

    def generate_usernames(self, num_results, *args, **kwargs):
        return [self.generate_username(*args, **kwargs) for _ in range(num_results)]
