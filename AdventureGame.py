#Game play class
from pathlib import Path

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
        return
    print("GOOD GAME!")
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
            play_Game(mod_path, player)
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

''')
    input("Input anything to return to the menu. ")