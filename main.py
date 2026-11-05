print("Welcome to my number guesing program")
print("Try and guess the number as it is from 1-50")
secret=32
guess=int(input("Enter your first guess"))
if guess-secret>=20:
    print("ice cold, you very far from the number.")
    if guess-secret<=15:
        print(" cold, you are far from the number.")
    if guess-secret==10:
        print("Warm, you are getting closer to the number.")
        if guess==32:
            print("Congrats, you have won the game.")


