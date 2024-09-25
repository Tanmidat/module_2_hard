n = int(input('Input number from 3 to 20: '))

def give_me_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password

result = give_me_password(n)
print('Password:', result)