#project 0
import sys
from pathlib import Path
import CharacterCreator as cc
import AdventureGame as ag

avatar =  cc.Avatar()
if(len(sys.argv)==1):
    exit_game=True
    while exit_game:
        choice = input('''Select one of the options:
    1. New game
    2. Choose character
    3. Upload character instructions
    4. Upload module instructions
    5. Exit
''')
        if choice == '0':
            break
        elif choice == '1':
            avatar.new_Character()
        elif choice == '2':
            char = avatar.choose_Character()
            if char!='0':
                ag.select_Module(avatar)
        elif choice == '3':
            avatar.upload_Character()
        elif choice == '4':
            ag.upload_Module()
        elif choice == '5':
            print('Thanks for Playing!')
            break
        else:
            print('Please type only the number of the option you wish to select.')
elif(len(sys.argv)<5):
    print('not enough arguments')
elif(len(sys.argv)==5):
    name = sys.argv[1]
    strg = sys.argv[2]
    agil = sys.argv[3]
    clvr = sys.argv[4]
    if name.isalpha() and strg.isdigit() and agil.isdigit() and clvr.isdigit():
        stats = [int(strg),int(agil),int(clvr)]
        if sum(stats) < 12:
            print('you need to allocate all 12 points to your skills.')
        elif sum(stats) > 12:
            print('you only have 12 skill points to allocate.')
        else:
            avatar.character_File(name,strg,agil,clvr,0)
    else:
        print('improper arguments: requires "name:string" "strength:int" "agility:int" "cleverness:int"')
else:
    print('too many arguments')

        