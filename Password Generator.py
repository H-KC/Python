import random
#BY -> HKC
print('Hello , and welcome to Password Generator .')
pwl = input("how long do You want Your Password to be : ")#pwl : Pass Word Length
let = input('how many characters : ')#let : lett
#num = input('how many numbers : ')

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz^?!?$%&/()=?`'+#*'~';:_,.-<>|"
password = ''

for letter in range(int(let)):
    password += str(letters[random.randint(0, 52)])

for number in range(int(pwl)-int(let)):
    password += str(random.randint(0, 9))
#converting String to list and shuffling the list then joining the list
# to be a String again .
l=list(password )
random.shuffle(l)
password =''.join(l)

print('your password is : ' + str(password))
