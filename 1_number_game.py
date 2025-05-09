def nearestMultiple(num):
    if num >= 4:
        near = num - (4 - (num % 4))
    else:
        near = 4
    return near

def lose():
    print("\n You Lose!")
    exit(0)



def consecutive(xyz):
    i = 1
    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!= 1:
            return False
        i = i + 1
    return True

def start(){
    xyz[] = 0
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
         print("\nEnter 'S' to take the second chance.")
          chance = input('> ')

    if chance == "F":
    
        while True:
            if last == 20:  # Ensure 'last' is defined before this condition
                lose()
            else:
                print("\nYour Turn")
                print("how many numbers you want to add?")
                inp = int(input("<"))

                if inp > 0 and inp <= 3:
                    com = 4 - inp

                else:
                    print("Wrong Input")
                    lose()

                i,j = 1,1

                print("Enter numbers")
                while i <= inp:
                    a = int(input("< "))
                    xyz.append(a)
                    i = i + 1

                last = xyz[-1]


                if consecutive(xyz) == True:
                    if last == 21
                        lose()
                    else:
                        while j<=com:
                            xyz.append(last+j)
                            j = j+1
                        print("Order of inputs after not input consecutive")
                        print(xyz)
                        last = xyz[-1]

                else:
                    print("Not consecutive inputs")
                    lose()
                    
    if chnace == "S":
        com = 1
        last = 0
        while last < 20:
            j = 1
            while j <= com:
                xyz.append(last +j)
                j = j+1
               print ("Order of inputs after computer's turn is:")
                print (xyz)
                if xyz[-1] == 20:
                    lose1()   

                else:
                print("\nYour turn.")
                print("\n How many numbers you want to enter")
                inp = 
}