weight = float(input("Weight: "))
what = input("(K)g or (L)bs: ")
if what == 'l' or what == 'L':
    converted = weight*0.45
    print(f"You weight {converted} kilograms")
    if converted > 100:
        print("Consider starting a diet ! ")
    elif converted < 40:
        print("Don't skip breakfast !")
    

elif what == 'k' or what == 'K':
    converted = weight*2.2
    print(f"You weight {converted} pounds")
    if converted > 220:
        print("Consider starting a diet !")
    elif converted < 88:
        print("Don't skip breakfast !")