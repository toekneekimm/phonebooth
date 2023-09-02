
#game name: phone booth
#creator: tony kim
#date: 9/2/2023 mm/dd/yy



import time
list=[]
number=[]
#ask activate or not


def printinglist(boom, ghost): #function for printing out name and number
    a=1
    if boom==[]:
        print("empty")
    for i in boom:
        print(f"{a}. {i} {ghost[a-1]}")
        a=a+1





print("initiating photobooth...")

file = open("C:\\Users\\user\\OneDrive\\Desktop\\photobooth.txt", "r") #when the photo booth starts, this code make sure the existing number shows up
while True:
    x = file.readline()
    if not x:
        break
    y=x.split() #splits the string into 2 
    list.append(y[0])
    number.append(y[1])






time.sleep(2)
while True:
    print("This is your current photobooth:") 
    printinglist(list, number) #shows current code
    choice=input("Do you want to add or delete? Type 'leave' to escape: ")
    if choice=="add": #add code
        add1=input("Who do you want to add?: ")
        list.append(add1)
        add2=input("What's his phone number?")
        number.append(add2)

        printinglist(list, number)
    elif choice=="delete":#delete code
        delete1=input("Who do you want to delete?: ")
        po=list.index(delete1)
        list.remove(delete1)
        number.remove(number[po])
        printinglist(list, number)
    elif choice=="leave": #quit code
        file= open("C:\\Users\\user\\OneDrive\\Desktop\\photobooth.txt", "w") #creates a file for the program
        for i in range(len(list)): 
            x= list[i]+" "+ number[i]+"\n"
            file.write(x)
        file.close()
        break
    else:
        print("Invalid Choice")
        print(choice)

        




