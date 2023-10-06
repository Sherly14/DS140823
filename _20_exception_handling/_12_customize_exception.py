class InvalidAgeError(Exception):

    # def __init__(self):
    #     print("InvalidAgeError: your age is less than 17, you are still a kid!")

    def __str__(self):
        return "your age is less than 17, you are still a kid!"