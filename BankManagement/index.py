import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    @classmethod
    def clean_data(cls):
        valid = []
        for i in cls.data:
            if all(k in i for k in ["name", "age", "email", "pin", "accountNo", "balance"]):
                valid.append(i)
        cls.data = valid
        cls.__update()
        print("✅ Corrupted records removed from database.\n")

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
            Bank.data = data
            clean_data = True
        else:
            print("⚠️ No data file found. Starting fresh.")
    except Exception as err:
        print(f"Exception: {err}")
        clean_data = False

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(Bank.data, indent=2))

    @classmethod
    def __accountgenerator(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*()", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age": int(input("Tell your age :- ")),
            "email": input("Tell your email :- "),
            "pin": int(input("Tell your 4-digit pin :- ")),
            "accountNo": Bank._Bank__accountgenerator(),
            "balance": 0,
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("❌ Sorry, you cannot create an account.")
        else:
            print("\n✅ Account created successfully! 🎉")
            for k, v in info.items():
                print(f"{k}: {v}")
            print("📌 Please note down your account number.")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        userdata = [
            i for i in Bank.data if i.get("accountNo") == accountNumber and i.get("pin") == pin
        ]
        if not userdata:
            print("❌ No matching account found.")
        else:
            print(f"Hello {userdata[0]['name']}!")
            amount = int(input("💰 Enter amount to deposit: "))
            if amount > 10000:
                print("❌ Amount exceeds limit (₹10,000).")
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print(f"✅ ₹{amount} deposited successfully!")

    def withdraw(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        userdata = [
            i for i in Bank.data if i.get("accountNo") == accountNumber and i.get("pin") == pin
        ]
        if not userdata:
            print("❌ No matching account found.")
        else:
            print(f"Hello {userdata[0]['name']}!")
            amount = int(input("💰 Enter amount to withdraw: "))
            if userdata[0]["balance"] < amount:
                print("❌ Insufficient balance.")
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print("✅ Amount withdrawn successfully!")

    def showdetails(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        userdata = [
            i for i in Bank.data if i.get("accountNo") == accountNumber and i.get("pin") == pin
        ]
        if not userdata:
            print("❌ No matching account found.")
        else:
            print("📄 Your account details:")
            for k, v in userdata[0].items():
                if k != "pin":
                    print(f"{k}: {v}")

    def updatedetails(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        userdata = [
            i for i in Bank.data if i.get("accountNo") == accountNumber and i.get("pin") == pin
        ]
        if not userdata:
            print("❌ No matching account found.")
        else:
            print("What do you want to update?\n1. Name\n2. Email")
            choice = int(input("Enter choice: "))
            if choice == 1:
                userdata[0]["name"] = input("Enter new name: ")
            elif choice == 2:
                userdata[0]["email"] = input("Enter new email: ")
            else:
                print("❌ Invalid choice.")
                return
            Bank.__update()
            print("✅ Details updated successfully!")

    def deleteaccount(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        index = -1
        for idx, i in enumerate(Bank.data):
            if i.get("accountNo") == accountNumber and i.get("pin") == pin:
                index = idx
                break
        if index == -1:
            print("❌ No matching account found.")
        else:
            confirm = input("⚠️ Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == "yes":
                del Bank.data[index]
                Bank.__update()
                print("✅ Account deleted successfully!")
            else:
                print("❎ Account deletion cancelled.")


# Menu
user = Bank()

# Clean corrupted data on load
if "clean_data" in locals() and clean_data:
    user.clean_data()

print("\n🧾 Welcome to Bank Management System\n")
print("Press 1 👉 Create a New Account")
print("Press 2 👉 Deposit Money")
print("Press 3 👉 Withdraw Money")
print("Press 4 👉 Show Account Details")
print("Press 5 👉 Update Account Details")
print("Press 6 👉 Delete Account")

try:
    check = int(input("\n📝 Tell your response (1-6): "))
    if check == 1:
        user.Createaccount()
    elif check == 2:
        user.depositmoney()
    elif check == 3:
        user.withdraw()
    elif check == 4:
        user.showdetails()
    elif check == 5:
        user.updatedetails()
    elif check == 6:
        user.deleteaccount()
    else:
        print("❌ Invalid input.")
except Exception as e:
    print(f"⚠️ Error: {e}")
=======
import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    @classmethod
    def clean_data(cls):
        valid = []
        for i in cls.data:
            if all(k in i for k in ["name", "age", "email", "pin", "accountNo", "balance"]):
                valid.append(i)
        cls.data = valid
        cls.__update()
        print("✅ Corrupted records removed from database.\n")

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
            Bank.data = data
            clean_data = True
        else:
            print("⚠️ No data file found. Starting fresh.")
    except Exception as err:
        print(f"Exception: {err}")
        clean_data = False

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(Bank.data, indent=2))

    @classmethod
    def __accountgenerator(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*()", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age": int(input("Tell your age :- ")),
            "email": input("Tell your email :- "),
            "pin": int(input("Tell your 4-digit pin :- ")),
            "accountNo": Bank._Bank__accountgenerator(),
            "balance": 0,
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("❌ Sorry, you cannot create an account.")
        else:
            print("\n✅ Account created successfully! 🎉")
            for k, v in info.items():
                print(f"{k}: {v}")
            print("📌 Please note down your account number.")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        userdata = [
            i for i in Bank.data if i.get("accountNo") == accountNumber and i.get("pin") == pin
        ]
        if not userdata:
            print("❌ No matching account found.")
        else:
            print(f"Hello {userdata[0]['name']}!")
            amount = int(input("💰 Enter amount to deposit: "))
            if amount > 10000:
                print("❌ Amount exceeds limit (₹10,000).")
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print(f"✅ ₹{amount} deposited successfully!")

    def withdraw(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        userdata = [
            i for i in Bank.data if i.get("accountNo") == accountNumber and i.get("pin") == pin
        ]
        if not userdata:
            print("❌ No matching account found.")
        else:
            print(f"Hello {userdata[0]['name']}!")
            amount = int(input("💰 Enter amount to withdraw: "))
            if userdata[0]["balance"] < amount:
                print("❌ Insufficient balance.")
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print("✅ Amount withdrawn successfully!")

    def showdetails(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        userdata = [
            i for i in Bank.data if i.get("accountNo") == accountNumber and i.get("pin") == pin
        ]
        if not userdata:
            print("❌ No matching account found.")
        else:
            print("📄 Your account details:")
            for k, v in userdata[0].items():
                if k != "pin":
                    print(f"{k}: {v}")

    def updatedetails(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        userdata = [
            i for i in Bank.data if i.get("accountNo") == accountNumber and i.get("pin") == pin
        ]
        if not userdata:
            print("❌ No matching account found.")
        else:
            print("What do you want to update?\n1. Name\n2. Email")
            choice = int(input("Enter choice: "))
            if choice == 1:
                userdata[0]["name"] = input("Enter new name: ")
            elif choice == 2:
                userdata[0]["email"] = input("Enter new email: ")
            else:
                print("❌ Invalid choice.")
                return
            Bank.__update()
            print("✅ Details updated successfully!")

    def deleteaccount(self):
        accountNumber = input("Enter your account number: ")
        pin = int(input("Enter your 4-digit pin: "))
        index = -1
        for idx, i in enumerate(Bank.data):
            if i.get("accountNo") == accountNumber and i.get("pin") == pin:
                index = idx
                break
        if index == -1:
            print("❌ No matching account found.")
        else:
            confirm = input("⚠️ Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == "yes":
                del Bank.data[index]
                Bank.__update()
                print("✅ Account deleted successfully!")
            else:
                print("❎ Account deletion cancelled.")


# Menu
user = Bank()

# Clean corrupted data on load
if "clean_data" in locals() and clean_data:
    user.clean_data()

print("\n🧾 Welcome to Bank Management System\n")
print("Press 1 👉 Create a New Account")
print("Press 2 👉 Deposit Money")
print("Press 3 👉 Withdraw Money")
print("Press 4 👉 Show Account Details")
print("Press 5 👉 Update Account Details")
print("Press 6 👉 Delete Account")

try:
    check = int(input("\n📝 Tell your response (1-6): "))
    if check == 1:
        user.Createaccount()
    elif check == 2:
        user.depositmoney()
    elif check == 3:
        user.withdraw()
    elif check == 4:
        user.showdetails()
    elif check == 5:
        user.updatedetails()
    elif check == 6:
        user.deleteaccount()
    else:
        print("❌ Invalid input.")
except Exception as e:
    print(f"⚠️ Error: {e}")

