def Main():
    start = int(input("Введите правую границу: "))
    end = int(input("Введите левую границу: "))

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)
Main()


def Main_2():
    start = int(input("Введите правую границу: "))
    end = int(input("Введите левую границу: "))

    for count in range(start, end + 1):
        if(count > 10):
            if(count%2==0 or count%3==0 or count%5==0 or count%7==0):
                #print("не простое")
                count+=1
            else:
                print(count)
        elif(count<=10 and count>=2):
            if((count//2>=2 or count//3>=2) and (count!=7 and count!=5)):
                #print("не простое")
                count+=1
            else:
                print(count)
Main_2()