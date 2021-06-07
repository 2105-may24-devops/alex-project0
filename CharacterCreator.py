#character creator class
from pathlib import Path
import os

def skill_tree():
    points = 12
    strong = input('Enter the amount of skill points you want to give to strength({0} left): '.format(points))
    if strong.isdigit() and int(strong) <= points and int(strong) >= 0:
        strong = int(strong)
        points-=strong
        agile = input('Enter the amount of skill points you want to give to agility({0} left): '.format(points))
        if agile.isdigit() and int(agile) <= points and int(agile) >= 0:
            agile = int(agile)
            points-=agile
            clever = input('Enter the amount of skill points you want to give to cleverness({0} left): '.format(points))
            if clever.isdigit() and int(clever) <= points and int(clever) >= 0:
                clever = int(clever)
                points-=clever
                if points==0 and (strong+agile+clever)==12:
                    return [strong, agile, clever]
                else:
                    print('Something went wrong allocating your skill points, please try again.')
            else:
                print('There was an error allocating your cleverness points, try allocating them again.')    
        else:
            print('There was an error allocating your agility points, try allocating them again.')
    else:
        print('There was an error allocating your strength points, try allocating them again.')

class Avatar:
    #constructor
    def __init__(self):
        self.file = ''
        self.name = 'Blank'
        self.strg = 0
        self.agil = 0
        self.clvr = 0
        self.bkmk = ''
        p = Path.cwd() / "AGcharacters"
        Path.mkdir(p, parents=True, exist_ok=True)
        dir_path = Path(p).relative_to(Path.cwd())
        self.fileParent = dir_path

    #File creator
    def character_File(self,n,s,a,c,b,r):
        file_name = n + '.txt'
        if r:
            file_parent = Path('AGcharacters')
        else:
            file_parent = self.fileParent
        file_path = file_parent / file_name
        Path.touch(file_path,exist_ok=True)
        self.file = file_path
        p = Path(file_path)
        lines = '''{0}
{1}
{2}
{3}
{4}
'''.format(n,s,a,c,b)
        p.write_text(lines)

    #print method
    def __str__(self):
        return ('''The hero {0} has:
strength: {1}
agility: {2}
cleverness: {3}'''.format(self.name,self.strg,self.agil,self.clvr))

    #Character creator
    def new_Character(self):

        #name assignment
        name = input('enter your name: ')
        if name == '0':
            return name
        print('your name is: '+ name)
        name_correct = input('is that correct? (y/n) ')
        if name_correct == '0':
            return name_correct
        while name_correct != 'y':
            name = input('Choose a different name: ')
            if name == '0':
                return name
            print('your name is:'+ name)
            name_correct = input('is that correct? (y/n) ')
            if name_correct == '0':
                return name_correct
        self.name = name
        print('The character '+ name +' has been created.')

        #skill point allocation
        print('Next we need to allocate your skill points across the 3 skills.')
        skills=[]
        while len(skills)==0:
            skills = skill_tree()
            if skills:
                    break
            else:
                skills=[]
        print('''Your current skills are:
strength: {0}
agility: {1}
cleverness: {2}'''.format(skills[0],skills[1],skills[2]))
        skills_correct = input('is that correct? (y/n) ')
        if skills_correct == '0':
            return skills_correct
        while skills_correct != 'y':
            skills=[]
            print('Please reallocate your skills.')
            while len(skills)==0:
                skills = skill_tree()
                if skills:
                    break
                else:
                    skills=[]
            print('''Your current skills are:
strength: {0}
agility: {1}
cleverness: {2}'''.format(skills[0],skills[1],skills[2]))
            skills_correct = input('is that correct? (y/n) ')
            if skills_correct == '0':
                return skills_correct
        self.strg = skills[0]
        self.agil = skills[1]
        self.clvr = skills[2]
        print('''The character {0} has had the following stats allocated:
strength: {1}
agility: {2}
cleverness: {3}
        '''.format(name,skills[0],skills[1],skills[2]))
        
        #Character File Creation
        bkmk=0
        self.character_File(name, self.strg, self.agil, self.clvr, bkmk, False)

    #Character select   
    def choose_Character(self):
        path = Path('AGcharacters')
        characters = []
        character_files=[]
        i=0
        for p in path.iterdir():
            if i==0:
                print("Character Select: ")
            i+=1
            character_files.append(p)
            pc = str(p)
            if pc.count('\\')!=0:
                pc = pc[pc.find('\\')+1:pc.find('.txt')]
            elif pc.count('/')!=0:
                pc = pc[pc.find('/')+1:pc.find('.txt')]
            else:
                print('Something is wrong with this character path: ')
                print(pc)
                return '0'
            print(str(i)+'. '+pc)
            characters.append(pc)
        print(str(i+1)+'. Exit')
        if characters:
            adventurer = input('Choose one of the above characters. ')
            if adventurer=='0' or adventurer==str(len(characters)+1):
                return '0'
            chosen_One = characters[int(adventurer)-1]
            print('Your chosen character is ' + chosen_One)
            character_correct = input('is that correct? (y/n) ')
            while character_correct != 'y':
                for x in range(i):
                    print(str(x+1)+'. '+characters[x])
                print(str(i+1)+'. Exit')
                adventurer = input('Choose one of the above characters. ')
                if adventurer=='0' or adventurer==str(len(characters)+1):
                    return '0'
                chosen_One = characters[int(adventurer)-1]
                print('Your chosen character is ' + chosen_One)
                character_correct = input('is that correct? (y/n) ')
            self.file = character_files[characters.index(chosen_One)]
            path = self.file
            with path.open() as f: 
                character_stats = f.readlines()
            i = 0
            for stat in character_stats:
                value = character_stats[i]
                if value.count('\n') != 0:
                    value = value[:value.find('\\')]
                character_stats[i] = value
                i+=1
            self.name = str(character_stats[0])
            self.strg = int(character_stats[1])
            self.agil = int(character_stats[2])
            self.clvr = int(character_stats[3])
            self.bkmk = str(character_stats[4])
            print(self.__str__())
        else:
            print("There aren't any characters available, try making one first.")
            return '0'
    #upload character instructions    
    def upload_Character(self):
        print('''To upload a character either call p0.py with the correct arguments, name, strength value, agility value, and cleverness value, the values should add to 12
or you can write the character into a .txt file in /AGcharacters that should look something like this: 

exampleName
5
4
3
0

Note:
    The .txt file should be named the same as the character name for easy reference, 
    The first 3 numeric values are digits that add up to 12, 
    The last digit should always be zero when creating a new character.
Once that is done you should be able to access your character from the "Choose character" option in the menu''')
        input("Input anything to return to the menu. ")
    def update_Character(self):
        if self.file == '':
            file_name = self.name + '.txt'
            file_parent = self.fileParent
            file_path = file_parent / file_name
            Path.touch(file_path,exist_ok=True)
            self.file = file_path
            p = Path(file_path)
        else:
            p = Path(self.file)
        lines = '''{0}
{1}
{2}
{3}
{4}
'''.format(self.name,self.strg,self.agil,self.clvr,self.bkmk)
        p.write_text(lines)
    def resurrect_Character(self):
        path = Path('AGgraveyard')
        characters = []
        character_files=[]
        i=0
        for p in path.iterdir():
            if i==0:
                print("Character Select: ")
            i+=1
            character_files.append(p)
            pc = str(p)
            if pc.count('\\')!=0:
                pc = pc[pc.find('\\')+1:pc.find('.txt')]
            elif pc.count('/')!=0:
                pc = pc[pc.find('/')+1:pc.find('.txt')]
            else:
                print('Something is wrong with this character path: ')
                print(pc)
                return '0'
            print(str(i)+'. '+pc)
            characters.append(pc)
        print(str(i+1)+'. Exit')
        if characters:
            adventurer = input('Choose one of the above characters. ')
            if adventurer=='0' or adventurer==str(len(characters)+1):
                return '0'
            chosen_One = characters[int(adventurer)-1]
            print('Your chosen character is ' + chosen_One)
            character_correct = input('is that correct? (y/n) ')
            while character_correct != 'y':
                for x in range(i):
                    print(str(x+1)+'. '+characters[x])
                print(str(i+1)+'. Exit')
                adventurer = input('Choose one of the above characters. ')
                if adventurer=='0' or adventurer==str(len(characters)+1):
                    return '0'
                chosen_One = characters[int(adventurer)-1]
                print('Your chosen character is ' + chosen_One)
                character_correct = input('is that correct? (y/n) ')
            self.file = character_files[characters.index(chosen_One)]
            path = self.file
            with path.open() as f: 
                character_stats = f.readlines()
            value = character_stats[0]
            if value.count('\n') != 0:
                value = value[:value.find('\\')]
            character_stats[0] = value
            name = str(character_stats[0])
        print('We need to reallocate your skill points across the 3 skills after being resurrected from the graveyard.')
        skills=[]
        while len(skills)==0:
            skills = skill_tree()
            if skills:
                    break
            else:
                skills=[]
        print('''Your current skills are:
strength: {0}
agility: {1}
cleverness: {2}'''.format(skills[0],skills[1],skills[2]))
        skills_correct = input('is that correct? (y/n) ')
        if skills_correct == '0':
            return skills_correct
        while skills_correct != 'y':
            skills=[]
            print('Please reallocate your skills.')
            while len(skills)==0:
                skills = skill_tree()
                if skills:
                    break
                else:
                    skills=[]
            print('''Your current skills are:
strength: {0}
agility: {1}
cleverness: {2}'''.format(skills[0],skills[1],skills[2]))
            skills_correct = input('is that correct? (y/n) ')
            if skills_correct == '0':
                return skills_correct
        self.strg = skills[0]
        self.agil = skills[1]
        self.clvr = skills[2]
        print('''The character {0} has had the following stats allocated:
strength: {1}
agility: {2}
cleverness: {3}
        '''.format(name,skills[0],skills[1],skills[2]))
        
        #Character File Creation and removal from graveyard
        bkmk=0
        self.character_File(name, self.strg, self.agil, self.clvr, bkmk, True)
        os.remove(Path(path).absolute())
