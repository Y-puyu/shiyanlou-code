for i in range(1,101):
    if i<7:
        print(i)
        continue
    elif i >=70 and i <= 79:
        continue
    elif not(i%7):
        continue
    elif not((i-7)%10):
        continue
    elif i>=70 and i<= 79:
        continue
    else:
        print(i)

