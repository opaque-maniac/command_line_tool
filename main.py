#import modules
import platform
import os
import shutil

home = os.getcwd()

#function to check type of os
def is_windows():
    a = platform.system()
    if "Windows" in a or "windows" in a:
        return True
    else:
        return False

#function to clear screen
def clear():
    if is_windows():
        statement = "cls"
    else:
        statement = "clear"
    os.system(statement)
    print("")
    
#function to list content of current woking directory
def ls(command):
    try:
        if len(command) > 3:
            if is_windows():
                path = os.getcwd() + '\\' + command[3:]
                os.listdir(path)
        else:
            for i in os.listdir():
                if "." in i:
                    status = " ~ file ~ \t"
                else:
                    status = " ~ folder ~ \t"
                print(status + " " + i)
    except:
        print("Invalid command entered")
    print("")
  
#function to change current working directory      
def change(command):
    try:
        if command[3:] == "..":
            os.chdir("..")
        elif command == "cd" or command == "cd ":
            os.chdir(home)
        else:
            if command[3:] in os.listdir():
                if is_windows():
                    new_directory = os.getcwd() +"\\"+command[3:]
                else:
                    new_directory = os.getcwd() + '/'+command[3:]
                os.chdir(new_directory)
            else:
                os.chdir(command[3:])
    except:
        print("Invalid comand entered :\n%s" % (command))
    print("")
    
#function to make directory    
def makedir(command):
    try:
        if len(command) > 6:
            os.mkdir(command[6:])
        else:
            print("Invalid command entered")
    except:
        print("Invalid command entered")
    print("")
    
#function to delete files and folders
def delete(command):
    try:
        target = command[3:]
        if "." in target:
            os.remove(target)
        else:
            shutil.rmtree(target)
    except:
        print("Invalid command entered")
    print("")
    
#function to display content of a file
def cat(command):
    try:
        if len(command) > 4:
            file = open(command[4:], 'r')
            for i in file.readlines():
                print(i)
        else:
            print("Invalid command entered")
    except:
        print("Invalid command entered")
        print("")
        
#function to create empty files
def create(command):
    try:
        if len(command) > 6:
            name = command[6:]
            with open(name, 'x') as file:
                pass
        else:
            pass
    except:
        print("Invalid command entered")
    print("")

#function to display help message
def helping(command):
    try:
        file = open('help.txt', 'r').readlines()
        if len(command) > 5:
            for i in file:
                if command[5:] and command[5:] in i:
                    print(i)
        else:
            for j in file:
                print(j)
    except:
        print("Invalid command entered or an error occured")
    print("")
    
#main function that accepts input and shows output
def interface():
    clear()
    while True:
        command = str(input("$~ "))
        if command == "pwd":
            print(os.getcwd(),"\n")
        elif command == "clear":
            clear()
        elif command[:2] == "ls":
            ls(command)
        elif "cd" in command:
            change(command)
        elif "mkdir" in command:
            makedir(command)
        elif "rm" in command:
            delete(command)
        elif command[:3] == "cat":
            cat(command)
        elif command[:5] == "touch":
            create(command)
        elif command[:4] == "help":
            helping(command)
        elif command == "exit":
            exit()
        else:
            print("Invalid command enterd\n")
            
#execution of main function
if __name__ == '__main__':
    interface()