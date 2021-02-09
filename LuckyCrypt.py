#coding:utf-8

#LuckyCrypt
#Version : 1.0
#Author : LuckySmile :)
#2021

#imports
import time
import os

def askValidText(what):
    fastPrint(f"What is the {what} you want to encrypt ? : ")
    msg = input()
    while msg == "":
        fastPrint("! Please write something : ")
        msg = input()
    #Check that user doesn't write forbidden characters (ex : 'ç' or 'è')
    #while not checkChars(msg):
    #    msg = input(f"! Please write a valid {what} : ")
    #    while msg == "":
    #        msg = input("! Please write something !")
    return msg

def askValidKey():
    fastPrint("Enter the key : ")
    key = input()
    while key == "":
        fastPrint("! Please write something :")
        key = input()
    while not checkChars(key):
        fastPrint("! Please enter a valid key : ")
        key = input()
        while key == "":
            fastPrint("! Please write something  : ")
            key=input()
    return key

def clearScreen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        print("[error] Couldn't find your OS name... Can't clear screen")

def fastPrint(msg):
    for letter in msg:
        if letter == '\n':
            print()
        else:
            print(letter, end='', flush=True)
            time.sleep(0.01)

def slowPrint(msg):
    for letter in msg:
        if letter == '\n':
            print()
        else:
            print(letter, end='', flush=True)
            time.sleep(0.1)
    time.sleep(1)

def checkChars(text):
    for letter in text:
        if ord(letter) < 32 or ord(letter) > 126:
            fastPrint("<error>")
            time.sleep(1)
            fastPrint(f" Character : [{letter}] Forbidden !")
            time.sleep(1)
            print()
            return False
    return True

def checkFile(file):
    with open(file, 'rt', encoding="utf-8") as file:
        for line in file:
            if not checkChars(line.rstrip("\n")):
                return False
    return True

def menu():
    clearScreen()
    print("Lucky Crypt v1.0")
    print("by LuckySmile :)")
    print('\n')
    fastPrint("1 : Encrypt\n")
    fastPrint("2 : Decrypt\n")
    fastPrint("3 : Encrypt file\n")
    fastPrint("4 : Decrypt file\n")
    fastPrint("0 : Quit\n")
    print()
    fastPrint("Make your choice : ")
    choice = input()
    if choice.lower() == "exit" or choice.lower() == "quit":
        choice = "0"
    while not choice.isdigit():
        fastPrint("! Please, enter a number : ")
        choice = input()
    choice = int(choice)
    while choice < 0 or choice > 4:
        fastPrint("! Please, enter a number between 0 and 4 : ")
        choice = input()
        if choice.lower() == "exit" or choice.lower() == "quit":
            choice = "0"
        while not choice.isdigit():
            fastPrint("! Please, enter a number : ")
            choice = input()
        choice = int(choice)
    return choice

def encrypt(msg, key):
    key = key.lower()
    for i in range(len(key)):
        if ord(key[i]) < 97:
            letterOrd = ord(key[i]) + 65
            while letterOrd > 122:
                letterOrd -= 26
            key = key.replace(key[i], chr(letterOrd))
        elif ord(key[i]) > 122:
            letterOrd = ord(key[i]) - 4
            while letterOrd < 97:
                letterOrd += 26
            key = key.replace(key[i], chr(letterOrd))
    encrypted = ""
    cpt = 0
    sub = 96
    for letter in msg:
        # If the char is not recognized, don't change it (ex : 'è' stays 'è')
        if ord(letter) >= 32 and ord(letter) <= 126:
            charEncrypted = ord(letter) + ord(key[cpt]) - 96
            if charEncrypted > 126:
                charEncrypted = charEncrypted - 95
        else:
            charEncrypted = ord(letter)
        # We stay in utf-8 (32 to 126), so for exemple if ord = 127 we want it to be 32
        
        encrypted += chr(charEncrypted)
        cpt += 1
        if cpt == len(key):
            cpt = 0
    return encrypted

def decrypt(msg, key):
    key = key.lower()
    for i in range(len(key)):
        if ord(key[i]) < 97:
            letterOrd = ord(key[i]) + 65
            while letterOrd > 122:
                letterOrd -= 26
            key = key.replace(key[i], chr(letterOrd))
        elif ord(key[i]) > 122:
            letterOrd = ord(key[i]) - 4
            while letterOrd < 97:
                letterOrd += 26
            key = key.replace(key[i], chr(letterOrd))
    for letter in key:
        if ord(letter) > 122:
            letter = chr(ord(letter) - 65)
            while ord(letter) < 97:
                letter = chr(ord(letter) + 26)
    decrypted = ""
    cpt = 0
    add = 96
    for letter in msg:
        # If the char is not recognized, don't change it (ex : 'è' stays 'è')
        if ord(letter) >= 32 and ord(letter) <= 126:
            charDecrypted = ord(letter) - ord(key[cpt]) + 96
            if charDecrypted < 32:
                charDecrypted = charDecrypted + 95
        else:
            charDecrypted = ord(letter)
        #We stay in utf-8 (32 to 126), so for exemple if ord = 31 we want it to be 126
        
        decrypted += chr(charDecrypted)
        cpt += 1
        if cpt == len(key):
            cpt = 0
    return decrypted

def saveMsg(mode, msg, result):
    first = "<error>"
    second = "<error>"
    if mode == "ENCRYPTED":
        first = "Original :"
        second = "Encrypted  :"
    else:
        first = "Encrypted   :"
        second = "Decrypted :"
    with open("Save.txt", 'w') as file:
        file.write(f"{first} {msg}\n{second} {result}")

def readFile(file):
    text = []
    with open(file, 'rt', encoding="utf-8") as file:
        for line in file:
            text.append(line.rstrip("\n"))
    return text

def encryptFile(file, key):
    encrypted = []
    with open(file, 'rt', encoding="utf-8") as file:
        for line in file:
            encrypted.append(encrypt(line.rstrip("\n"), key))
    return encrypted

def decryptFile(file, key):
    decrypted = []
    with open(file, 'rt', encoding="utf-8") as file:
        for line in file:
            decrypted.append(decrypt(line.rstrip("\n"), key))
    return decrypted

def saveFile(mode, file, result):
    if mode == "ENCRYPT":
        newFile = f"{file[:-4]}-encrypted.txt"
    else:
        newFile = f"{file[:-4]}-decrypted.txt"
    with open(newFile, 'wt', encoding="utf-8") as file:
        for i in range(len(result)):
            if i < len(result)-1:
                file.write(f"{result[i]}\n")
            else:
                file.write(result[i])

def choice1():
    clearScreen()
    print("Lucky Crypt v1.0")
    print("by LuckySmile :)\n")
    slowPrint("< Encrypt >")
    print('\n')
    msg = askValidText("sentence")
    key = askValidKey()
    encrypted = encrypt(msg, key)
    print()
    fastPrint("Original  : ")
    time.sleep(1)
    fastPrint(msg)
    time.sleep(1)
    print()
    fastPrint("Encrypted : ")
    time.sleep(1)
    fastPrint(encrypted)
    time.sleep(1)
    print('\n')
    fastPrint("Do you want to save it in [Save.txt] ? (Y/N) : ")
    save = input()
    while save.lower() != 'y' and save.lower() != 'n':
        fastPrint("! Please enter 'Y' or 'N' : ")
        save = input()
    if save.lower() == 'y':
        print()
        saveMsg("ENCRYPTED", msg, encrypted)
        fastPrint("Your data has been saved in [Save.txt] !")
        time.sleep(1)
        print('\n')
        fastPrint("Press enter to continue...")
        enter = input()
    
def choice2():
    clearScreen()
    print("Lucky Crypt v1.0")
    print("by LuckySmile :)\n")
    slowPrint("< Decrypt >")
    print('\n')
    msg = askValidText("encrypted sentence")
    key = askValidKey()
    decrypted = decrypt(msg, key)
    print()
    fastPrint("Encrypted : ")
    time.sleep(1)
    fastPrint(msg)
    time.sleep(1)
    print()
    fastPrint("Decrypted : ")
    time.sleep(1)
    fastPrint(decrypted)
    time.sleep(1)
    print('\n')
    fastPrint("Do you want to save it in [Save.txt] ? (Y/N) : ")
    save = input()
    while save.lower() != 'y' and save.lower() != 'n':
        save = input("! Please enter 'Y' or 'N' : ")
    if save.lower() == 'y':
        print()
        saveMsg("DECRYPTED", msg, decrypted)
        fastPrint("Your data has been saved in [Save.txt] !")
        time.sleep(1)
        print('\n')
        fastPrint("Press enter to continue...")
        enter = input()

def choice3():
    clearScreen()
    print("Lucky Crypt v1.0")
    print("by LuckySmile :)\n")
    slowPrint("< Encrypt file >")
    print('\n')
    cpt = 0
    foundFiles = []
    for file in os.listdir():
        if file.endswith(".txt") and file != "Save.txt":
            foundFiles.append(file)
            fastPrint(f"{cpt+1} : [{file}]")
            print()
            cpt += 1
    if cpt == 0:
        fastPrint("! No files detected...")
        print('\n')
        fastPrint(f"Please move the file yout want to encrypt in this directory :\n[{os.path.dirname(os.path.abspath(__file__))}]")
        print('\n')
        fastPrint("(And make sure this is a [.txt] file)")
        print('\n')
        fastPrint("Press enter to continue...")
        enter = input()
    else:
        fastPrint("0 : exit")
        print()
        print()
        fastPrint(f"{cpt} files detected")
        print('\n')
        file = input("Which file do you want to encrypt ? : ")
        while file == "":
            fastPrint("! Please write something : ")
            file = input()
        while file.isdigit():
            checkNb = int(file)
            if checkNb == 0:
                file = "0.txt"
            elif checkNb > 0 and checkNb <= len(foundFiles):
                file = foundFiles[checkNb-1]
            else:
                fastPrint(f"! Please, enter a number between 0 and {len(foundFiles)} : ")
                file = input()
        if not file.endswith(".txt"):
            file += ".txt"
        while not os.path.exists(f"{file}") and file != "0.txt" and file != "exit.txt" and file != "quit.txt":
            fastPrint(f"! The file [{file}] doesn't exist here, try again : ")
            file = input()
            while file == "":
                fastPrint("! Please write something : ")
                file = input()
            while file.isdigit():
                checkNb = int(file)
                if checkNb == 0:
                    file = "0.txt"
                elif checkNb > 0 and checkNb <= len(foundFiles):
                    file = foundFiles[checkNb-1]
                else:
                    fastPrint(f"! Please, enter a number between 0 and {len(foundFiles)} : ")
                    file = input()
            if not file.endswith(".txt"):
                file += ".txt"
        if file != "0.txt" and file != "exit.txt" and file != "quit.txt":
            print()
            key = askValidKey()
            clearScreen()
            text = readFile(file)
            encrypted = encryptFile(file, key)
            fastPrint("Original :")
            time.sleep(1)
            print()
            for line in text:
                fastPrint(line)
                print()
            time.sleep(1)
            print()
            fastPrint("Encrypted :")
            time.sleep(1)
            print()
            for line in encrypted:
                fastPrint(line)
                print()
            time.sleep(1)
            print()
            print()
            fastPrint(f"Do you want to save it in [{file[:-4]}-encrypted.txt] ? (Y/N) : ")
            save = input()
            while save.lower() != 'y' and save.lower() != 'n':
                fastPrint("! Please enter 'Y' or 'N' : ")
                save = input()
            if save.lower() == 'y':
                saveFile("ENCRYPT", file, encrypted)
                print()
                fastPrint(f"Encrypted file saved in [{file[:-4]}-encrypted.txt]")
                print('\n')
                fastPrint("Press enter to continue...")
                enter = input()

def choice4():
    clearScreen()
    print("Lucky Crypt v1.0")
    print("by LuckySmile :)\n")
    slowPrint("< Decrypt file >")
    print('\n')
    cpt = 0
    foundFiles = []
    for file in os.listdir():
        if file.endswith(".txt") and file != "Save.txt":
            foundFiles.append(file)
            fastPrint(f"{cpt+1} : [{file}]")
            print()
            cpt += 1
    if cpt == 0:
        fastPrint("! No files detected...")
        print('\n')
        fastPrint(f"Please move the file yout want to decrypt in this directory :\n[{os.path.dirname(os.path.abspath(__file__))}]")
        print('\n')
        fastPrint("(And make sure this is a [.txt] file)")
        print('\n')
        fastPrint("Press enter to continue...")
        enter = input()
    else:
        fastPrint("0 : exit")
        print()
        print()
        fastPrint(f"{cpt} files detected")
        print('\n')
        fastPrint("Which file do you want to decrypt ? : ")
        file = input()
        while file == "":
            fastPrint("! Please write something : ")
            file = input()
        while file.isdigit():
            checkNb = int(file)
            if checkNb == 0:
                file = "0.txt"
            elif checkNb > 0 and checkNb <= len(foundFiles):
                file = foundFiles[checkNb-1]
            else:
                fastPrint(f"! Please, enter a number between 0 and {len(foundFiles)} : ")
                file = input()
        if not file.endswith(".txt"):
            file += ".txt"
        while not os.path.exists(f"{file}") and file != "0.txt" and file != "exit.txt" and file != "quit.txt":
            fastPrint(f"! The file [{file}] doesn't exist here, try again : ")
            file = input()
            while file == "":
                fastPrint("! Please write something : ")
                file = input()
            while file.isdigit():
                checkNb = int(file)
                if checkNb == 0:
                    file = "0.txt"
                elif checkNb > 0 and checkNb <= len(foundFiles):
                    file = foundFiles[checkNb-1]
                else:
                    fastPrint(f"! Please, enter a number between 0 and {len(foundFiles)} : ")
                    file = input()
            if not file.endswith(".txt"):
                file += ".txt"
        if file != "0.txt" and file != "exit.txt" and file != "quit.txt":
            print()
            key = askValidKey()
            clearScreen()
            text = readFile(file)
            decrypted = decryptFile(file, key)
            fastPrint("Encrypted :")
            time.sleep(1)
            print()
            for line in text:
                fastPrint(line)
                print()
            time.sleep(1)
            print()
            fastPrint("Decrypted :")
            time.sleep(1)
            print()
            for line in decrypted:
                fastPrint(line)
                print()
            time.sleep(1)
            print('\n')
            fastPrint(f"Do you want to save it in [{file[:-4]}-decrypted.txt] ? (Y/N) : ")
            save = input()
            while save.lower() != 'y' and save.lower() != 'n':
                fastPrint("! Please enter 'Y' or 'N' : ")
                save = input()
            if save.lower() == 'y':
                saveFile("DECRYPT", file, decrypted)
                print()
                fastPrint(f"Decrypted file saved in [{file[:-4]}-decrypted.txt]")
                print('\n')
                fastPrint("Press enter to continue...")
                enter = input()

if __name__ == "__main__":
    choice = menu()
    while choice != 0:
        if choice == 1:
            choice1()
        elif choice == 2:
            choice2()
        elif choice == 3:
            choice3()
        elif choice == 4:
            choice4()
        else:
            choice = 0
            fastPrint("<error> Exiting program...")
            time.sleep(2)
        choice = menu()
    clearScreen()
    print("Lucky Crypt v1.0")
    print("by LuckySmile :)\n")
    slowPrint("See you ! :)")
    clearScreen()
