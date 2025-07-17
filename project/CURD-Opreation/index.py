from pathlib import Path
import os


def readfileandfolder():
    path = Path("")
    items = list(path.rglob("*"))
    for i, items in enumerate(items):
        print(f"{i+1} :{items}")


def createFile():
    try:
        readfileandfolder()
        name = input("please tell your file name :-")
        p = Path(name)
        if not p.exists():

            with open(p, "w") as fs:
                data = input("what you want to write in this file:-")
                fs.write(data)
            print(f"FILE CREATED SUCESSFULLY🎉🎉")

        else:
            print(f"This File Already Created")
    except Exception as err:
        print(f"An Error Occured as {err}")


def readfile():
    try:
        readfileandfolder()

        name = input("Which file want to read :")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print("Readed Successfully🎉")
        else:
            print("The file  doesnot exist")
    except Exception as err:
        print(f"Error occured as {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("tell which file you want to update :-")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file:-")
            print("press 2 for overwriting the data ")
            print("press 3 for apppeding some content in file ")
            res = int(input("tell your response :-"))
            if res == 1:
                name2 = input("tell your new file name :- ")
                p2 = Path(name2)
                p.name(p2)

            if res == 2:
                with open(p, "w") as fs:
                    data = input(
                        "tell what you want to write this is overwrite the data :-"
                    )
                    fs.write(data)
            if res == 3:
                with open(p, "a") as fs:
                    data = input("tell what you what to append :-")
                    fs.write(" " + data)
    except Exception as err:
        print("An error is {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete :-")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file removes Sucessfully")
        else:
            print("No such file is Exist")

    except Exception as err:
        print("As error is {err}")


print("press 1 for create a file")
print("press 2 for read a file")
print("press 3 for update a file")
print("press 4 for delete a file")
check = int(input("please tell you responce:-"))
if check == 1:
    createFile()
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()
