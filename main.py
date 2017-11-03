import random

def draw(a, b):
    secret_number = random.randint(a, b)
    #print(secret_number)

    win = False
    while win == False:
        try:
            user_number = int(input('Please get number between '+ str(a+1) + ' and ' + str(b-1) + ': '))
        except ValueError:
            print("Please enter a number.")
            continue
        if user_number == secret_number:
            print('Excelent!')
            win = True
        elif not a < user_number < b:
            print('Bad')
        elif user_number < secret_number:
            print ('Higher')
        elif user_number > secret_number:
            print('Lower')

if __name__ == '__main__':
    draw(0, 11)