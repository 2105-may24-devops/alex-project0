#Game play class
from pathlib import Path
import random
import os

def dungeon_Master(dm):
    if Path(dm).exists():
        dungeon_manual = dm.read_text()
        bestiary = dungeon_manual.split('\n')
        dungeon_module = {}
        encounter = []
        i = 0
        for m in bestiary:
            #skip empty lines
            if len(m)==0:
                continue
            #module key for character placement bookmarking
            elif m[0]=='|':
                key = m[1]
            else:
                #story elements
                if m[0]=='&':
                    if m[1].isdigit():
                        i = int(m[1])
                        encounter = [m[2:]]
                    else:
                        encounter[0] = dungeon_module[i][0]+'\n'+m[1:]
                #choices
                elif m[0]=='!' or m[0]=='*' or m[0]=='@' or m[0]=='$':
                    encounter.append(m[0:])
                dungeon_module[i] = encounter
        return dungeon_module, key
    else:
        print("Error: Game Module could not be found.")
        return '0', '0'
def play_Game(dm,pc):
    dm, key = dungeon_Master(dm)
    if key == '0':
        return True
    bookmark = str(pc.bkmk)
    if bookmark.count(key)!=0:
        page = int(bookmark[bookmark.find(key)+1])
        game_Save = True
        if page == 0:
            print("Save not found. Starting new game.")
            game_Save = False
        while game_Save:
            bookmark_correct = input("Continue game? (y/n)")
            if bookmark_correct == 'y':
               break 
            else:
                bookmark_correct = input("Are you sure you wish to start from the beginning? (y/n)")
                if bookmark_correct == 'y':
                    page = 0
                    break
    else:
        page = 0
        print("Save not found. Starting new game.")
    campaign=True
    while campaign:
        encounter = dm[page]
        #setting the scene
        scene = encounter[0]
        if scene.count('=') != 0:
            print(scene[:scene.find('=')])
            print("THE END")
            bookmark=bookmark[:bookmark.find(key)]+key+'0'+bookmark[bookmark.find(key)+2:]
            pc.bkmk = bookmark
            return True
        elif scene.count('~') != 0:
            print(scene[:scene.find('~')])
            print("GAME OVER")
            bookmark=bookmark[:bookmark.find(key)]+key+'0'+bookmark[bookmark.find(key)+2:]
            pc.bkmk = bookmark
            dead = pc.file
            file_path = Path.cwd() / "AGgraveyard"
            Path.mkdir(file_path, parents=True, exist_ok=True)
            grave_path = Path(file_path).relative_to(Path.cwd())
            pc.fileParent = grave_path
            file_name = pc.name + '.txt'
            file_parent = pc.fileParent
            file_path = file_parent / file_name
            Path.touch(file_path,exist_ok=True)
            pc.file = file_path
            pc.strg = 0
            pc.agil = 0
            pc.clvr = 0
            pc.update_Character()
            os.remove(Path(dead).absolute())
            print("Your character has been killed, either make a new one or resurrect them from the graveyard.")
            return False
        else:   
            print(scene)
            page+=1
        #showing your options
        choice_unresolved = True
        while choice_unresolved:
            plan = []
            for i in range(1, len(encounter)):
                plan.append(encounter[i])
                o = encounter[i]
                if o[0] =='!':
                    option = o[1:o.find('^')]
                else:
                    if o[2].isdigit():
                        option = o[3:o.find('^')]
                    else:
                        option = o[2:o.find('^')]
                print(str(i)+'. '+option)
            print(str(i+1)+'. Character stats')
            #getting input
            choice = input("What do you do? ")
            if choice == '0':
                bookmark = bookmark[:bookmark.find(key)]+key+str(page)+bookmark[bookmark.find(key)+2:]
                pc.bkmk = bookmark
                break
            elif choice == str(i+1):
                print(pc.__str__())
            else:
                choice_unresolved = False
        if choice == '0':
                break
        #resolving skills
        x=0
        p = plan[int(choice)-1]
        #strength check
        x = p.find('^')
        r = random.randint(1, 20)
        c = 0
        if p[1].isdigit() and p[2].isdigit():
            c = (int(p[1])*10)+int(p[2])
        elif p[1].isdigit():
            c = int(p[1])
        if p[0]=='*':
            print("Need to beat a "+str(c)+", you rolled a "+str((r+pc.strg))+".")
            if c <= (r+pc.strg):
                next = p[x+1]
                if p.count('+') != 0:
                    pc.strg+=int(p[x+3])
                    print("Nice! you got a +"+p[x+3]+" bonus to your strength stat.")
            else:
                n = p[x+1:]
                next = n[n.find('^')+1]
                if p.count('-') != 0:
                    pc.strg-=int(p[p[x+1:].find('^')+3])
                    print("Bad luck! you got a -"+p[x+3]+" penalty to your strength stat.")
        #agility check
        elif p[0]=='@':
            print("Need to beat a "+str(c)+", you rolled a "+str((r+pc.agil))+".")
            if c <= (r+pc.agil):
                next = p[x+1]
                if p.count('+') != 0:
                    pc.agil+=int(p[x+3])
                    print("Nice! you got a +"+p[x+3]+" bonus to your agility stat.")
            else:
                n = p[x+1:]
                next = n[n.find('^')+1]
                if p.count('-') != 0:
                    pc.agil-=int(p[p[x+1:].find('^')+3])
                    print("Bad luck! you got a -"+p[x+3]+" penalty to your agility stat.")
        #cleverness check
        elif p[0]=='$':
            print("Need to beat a "+str(c)+", you rolled a "+str((r+pc.clvr))+".")
            if c <= (r+pc.clvr):
                next = p[x+1]
                if p.count('+') != 0:
                    pc.clvr+=int(p[x+3])
                    print("Nice! you got a +"+p[x+3]+" bonus to your cleverness stat.")
            else:
                n = p[x+1:]
                next = n[n.find('^')+1]
                if p.count('-') != 0:
                    pc.clvr-=int(p[p[x+1:].find('^')+3])
                    print("Bad luck! you got a -"+p[x+3]+" penalty to your cleverness stat.")
        #ordinary decision
        else:
            next = p[x+1]
            if p.count('+') != 0:
                    if p[x+3]=='*':
                        pc.strg+=int(p[p.find('*')+1])
                        print("Nice! you got a +"+p[p.find('$')+1]+" bonus to your strength stat.")
                    elif p[x+3]=='@':
                        pc.agil+=int(p[p.find('@')+1])
                        print("Nice! you got a +"+p[p.find('$')+1]+" bonus to your agility stat.")
                    elif p[x+3]=='$':
                        pc.clvr+=int(p[p.find('$')+1])
                        print("Nice! you got a +"+p[p.find('$')+1]+" bonus to your cleverness stat.")
            if p.count('-') != 0:
                    if p[x+3]=='*':
                        pc.strg-=int(p[p.find('*')+1])
                        print("Bad luck! you got a -"+p[p.find('$')+1]+" penalty to your strength stat.")
                    elif p[x+3]=='@':
                        pc.agil-=int(p[p.find('@')+1])
                        print("Bad luck! you got a -"+p[p.find('$')+1]+" penalty to your agility stat.")
                    elif p[x+3]=='$':
                        pc.clvr-=int(p[p.find('$')+1])
                        print("Bad luck! you got a -"+p[p.find('$')+1]+" penalty to your cleverness stat.")
        #redirection
        page = int(next)
        pc.update_Character()
    return True
def select_Module(player):
    p = Path.cwd() / "AGmodules"
    Path.mkdir(p, parents=True, exist_ok=True)
    dir_path = Path(p).relative_to(Path.cwd())
    exit_module=True
    while exit_module:
        modules = []
        module_files=[]
        i=0
        for p in dir_path.iterdir():
            if i==0:
                print("Game Module Select: ")
            i+=1
            module_files.append(p)
            pc = str(p)
            if pc.count('\\')!=0:
                pc = pc[pc.find('\\')+1:pc.find('.txt')]
            elif pc.count('/')!=0:
                pc = pc[pc.find('/')+1:pc.find('.txt')]
            else:
                print('Something is wrong with this module path: ')
                print(pc)
                return '0'
            print(str(i)+'. '+pc)
            modules.append(pc)
        print(str(i+1)+'. Exit')
        if modules:
            mission = input('Choose one of the above modules. ')
            if mission == '0' or mission==str(len(modules)+1):
                break
            quest = modules[int(mission)-1]
            print('Your chosen game module is ' + quest)
            module_correct = input('is that correct? (y/n) ')
            while module_correct != 'y':
                for x in range(i):
                    print(str(x+1)+'. '+modules[x])
                print(str(i+1)+'. Exit')
                mission = input('Choose one of the above modules. ')
                if mission == '0' or mission==str(len(modules)+1):
                    break
                quest = modules[int(mission)-1]
                print('Your chosen game module is ' + quest)
                module_correct = input('is that correct? (y/n) ')
            if mission == '0' or mission==str(len(modules)+1):
                    break
            mod_path = module_files[modules.index(quest)]
            exit_module = play_Game(mod_path, player)
        else:
            print('Error: No modules found')
            break
def upload_Module():
    p = Path.cwd() / "AGmodules"
    Path.mkdir(p, parents=True, exist_ok=True)
    dir_path = Path(p).relative_to(Path.cwd())
    modules = []
    modules = []
    module_files=[]
    i=0
    for p in dir_path.iterdir():
        if i==0:
            print("Current Game Modules: ")
        i+=1
        module_files.append(p)
        pc = str(p)
        if pc.count('\\')!=0:
            pc = pc[pc.find('\\')+1:pc.find('.txt')]
        elif pc.count('/')!=0:
            pc = pc[pc.find('/')+1:pc.find('.txt')]
        else:
            print('Something is wrong with this module path: ')
            print(pc)
            return '0'
        print(str(i)+'. '+pc)
        modules.append(pc)
    print('''To upload a module either find one that is already made and add it to the /AGModules folder
or you can write your own into a .txt file in /AGcharacters that follows these syntax rules: 
|* Signifies a key which should always be the very first line of any module and should be a '|' followed by a character unique from other modules. i.e. |@
# comment that is ignored by the game
&Story element that should set the scene and lead to a decision needing to be made
!basic decision element
*#strength decision
@#agility decision
$#cleverness decision
    for all the skill decisions the # represents a positive number that player needs to roll equal to or greater than to beat.
    Also keep in mind that 
''')
    input("Input anything to return to the menu. ")