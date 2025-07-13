def createFile():
    try:
        readfileandfolder()
        name = input("please tell your file name :-")
        p = Path(name)
        if not p.exists() and p.is_file():

            with open(p, "w") as fs:
                data = input("what you want to write in this file:-")
                fs.write(data)
            print(f"FILE CREATED SUCESSFULLY🎉🎉")

        else:
            print(f"This File Already Created")
    except Exception as err:
        print(f"An Error Occured as {err}")
