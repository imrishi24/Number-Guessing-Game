import random
n=random.randint(1,20)
ng=1
print("The Number is between 1 and 20")
while(ng<=9):
    gn=int(input("Guess the number: \n"))
    if gn < n:
        print("Guess the number greater than",gn)
    elif gn > n:
        print("Guess the number lesser than",gn)
    else:
        print("you guessed the correct number\n")
        print(ng,"Guesses you took to to guess")
        break
    print(9-ng,"guesses left")
    ng=ng+1
if(n>9):
        print("game Over\n")