n = int(input())

if n//3 == 1:
    print("spring")
else:
    if n//3 == 2:
        print("summer")
    else:
        if n//3 == 3:
            print("fall")
        else:
            if n//3 == 4 or 1:
                print("winter")