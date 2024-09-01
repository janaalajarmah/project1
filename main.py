num=50
i=int(input('Guss a number betweeen 1 and 50:'))

for i in range(1,50):
 if i<num:
    print("Too low. Try again!")
 else:
    print("Well guessed!")
    break
 GussTheNumber()