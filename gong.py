print("="*3,"Welcome to songer Recorder","="*3)
menu1 = {}
menu1List = []
menu2List = []
menu3List = []

c = 0
while True:
    print(" *** MENU ***")
    print("1 Add a singer and a song")
    print("2 Add a song")
    print("3 Show all singer and songs")
    print("Q. to exti")
    numMenu = input("Please select a menu: ")

    if numMenu == '1':
        print("1")
        name = input("person: ")
        song = input("Song: ")
        menu1[name] = menu1List
        print(menu1)

    elif numMenu == '2':
        print("2")
        for i in menu1:
            c+=1
            menu2List.append(i)
            print(c,i)

        numperson = int(input(" Select Number Person: "))
        index = menu2List[numperson - 1]
        print(index)
        song = input("You’re selected singer" +str(index)+": ")
        menu3List.append(song)
        menu1[index] = menu3List
        
        
        print("Song added to",index)

    elif numMenu == '3':
        for i, v in menu1.items():
            pass

    elif  numMenu == 'q':
        break

print(menu1List)
print(menu1)
