from cryptography.fernet import Fernet
'''def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)'''



def load_key():
    file = open ("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_password = input("Enter your password: ")
key = load_key() + master_password.encode()
fer = Fernet(key)



def view():
    with open ("password.txt" , 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            
            user, passw = data.split("|")
            print("User: ",user ,"| Password: ",(fer.decrypt(passw.encode()).decode) )
def add():
    user_name = input("Enter your name: ")
    user_pwd = input("Enter your password: ")

    
    with open("password.txt", 'a') as f:
        f.write(user_name + "|" + (fer.encrypt(user_pwd.encode()).decode()) + "\n")
        
while True:
    user_input = input('''Select option --->
1) Add a new password
2) View an existing password
3) Exit\nEnter number: ''')
    if user_input == "3":
        break
    
    if user_input == "1":
        add()
    elif user_input == "2":
        view()
    
    else:
        print("Invalid input!")
    