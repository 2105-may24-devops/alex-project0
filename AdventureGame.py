#Game play class
from pathlib import Path

def play_Game(dm,pc):
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
            pc = pc[pc.find('\\')+1:pc.find('.txt')]
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