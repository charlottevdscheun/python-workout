import string
def create_password_checker(min_uppercase: int, min_lowercase: int, min_punctuation: int, min_digits: int):
    def check_password(password: str) -> string:
        password_results = {
            'uppercase': sum(1 for c in password if c.isupper()) - min_uppercase,
            'lowercase': sum(1 for c in password if c.islower()) - min_lowercase,
            'punctuation': sum(1 for c in password if c in string.punctuation) - min_punctuation,
            'digits': sum(1 for c in password if c.isdigit()) - min_digits
        }

        result = len([v for k, v in password_results.items() if v < 0])==0

        return result, password_results
    return check_password

pc1 = create_password_checker(2, 3, 1, 4)
print(pc1('Ab!1'))
print(pc1('ABcde!1234'))