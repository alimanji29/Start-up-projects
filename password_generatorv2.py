import random as rand
import pyperclip

def generate_password():#generates a randomly arranged value using ASCII format
    uppercaseLetter = chr(rand.randint(65, 90))
    uppercaseLetter2 = chr(rand.randint(65, 90))
    uppercaseLetter3 = chr(rand.randint(65, 90))
    lowercaseletter = chr(rand.randint(97, 122))
    lowercaseletter4 = chr(rand.randint(97, 122))
    lowercaseletter3 = chr(rand.randint(97, 122))
    lowercaseletter2 = chr(rand.randint(97, 122))
    lowercaseletter1 = chr(rand.randint(97, 122))
    symbol = chr(rand.randint(33, 47))
    symbol2 = chr(rand.randint(33, 47))
    symbol1 = chr(rand.randint(33, 47))
    digit = chr(rand.randint(48, 57))
    digit1 = chr(rand.randint(48, 57))
    password = f"{uppercaseLetter}{uppercaseLetter2}{uppercaseLetter3}{lowercaseletter}{lowercaseletter1}{lowercaseletter2}{lowercaseletter3}{lowercaseletter4}{symbol}{symbol1}{symbol2}{digit}{digit1}"
    return password

def check_password_strength(password):#used to check the strength of the password
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1#increments if condition is fulfilled
    else:
        feedback.append("Password should be at least 8 characters long.")# responses to the creator on ways to improve the password, which will all be compilied later

    has_uppercase = any(p.isalpha() and p.isupper() for p in password)#used to check if the condition is met inside the value
    if has_uppercase:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    has_lowercase = any(p.isalpha() and p.islower() for p in password)
    if has_lowercase:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    has_digit = any(p.isdigit() for p in password)
    if has_digit:
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    has_symbol = any(p in "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~" for p in password)
    if has_symbol:
        score += 1
    else:
        feedback.append("Password should contain at least one symbol (e.g., !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~).")

    common_patterns = ["123", "abc", "password"]
    has_common_pattern = any(pattern in password.lower() for pattern in common_patterns)
    if not has_common_pattern:
        score += 1
    else:
        feedback.append("Avoid common patterns like '123', 'abc', or 'password'.")

    if score == 6:#what each score means
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

print("Welcome to a password strength checker")
pas = input("Would you like to proceed with generating a password and checking its strength or would you like to make your own password and check its strength (y/n/o): ").lower().strip()

if pas == 'y':
    password = generate_password()#runs the func
    password_list = list(password)#converts it to a list since .shuffle cant do its business on anything but a list(lame)
    rand.shuffle(password_list)#randomly shuffles the randomly produced password
    shuffled_password = ''.join(password_list)#converts list characters into a string without any seperators
    print(f"Your generated password is: {shuffled_password}")#pretty obvious what this does
    pyperclip.copy(shuffled_password)  #copies the password to ppls clipboard

    p = input("Would you like to check the strength of the above password? (y/n): ").lower().strip()
    if p == 'y':
        strength, feedback = check_password_strength(shuffled_password)#runs the strength check
        print(f"Password Strength: {strength}")
        if feedback:
            print("Feedback:")
            for message in feedback:
                print(f"- {message}")
        else:
            print("No feedback required!")
    else:
        print("Why not? :(")

elif pas == 'o': 
    y = input("Type in your own password: ")#for people who think they are too good for the automatically generated password 
    strength, feedback = check_password_strength(y)
    print(f"Your password strength: {strength}")
    if feedback:
        print("Feedback:")
        for message in feedback:
            print(f"- {message}")
    else:
        print("No feedback required!")

else:
    print("Why even open this?")
