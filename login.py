from const import user_database



def check_if_user_exist(username, password):
    if username in user_database:
        if user_database[username] == password:
            return True
        else:
            print("wrong password. try again")
            return False
    else:
        print("username not in database")
        return False



def add_new_user(username,password):
    if username not in user_database:
        user_database[username]=password
        return True
    else:
        print("username already in database, try login instead")
        return False



def add_or_login():
    is_user_valid = False
    add_log = input("do you want to login or add new account:")
    while add_log != 'add' and add_log != 'login':
        print("please only type add or login")
        add_log = input("do you want to login or add new account:")
    if add_log == 'login':
        while is_user_valid==False:
            username = input("enter username:")
            password = input("enter password:")
            if check_if_user_exist(username, password) == True:
                print(f"login successful welcome back {username}")
                is_user_valid=True
                return True


    if add_log == 'add':
        username = input("enter username:")
        password = input("enter password:")
        if add_new_user(username,password):
            return username
        else:
            return False



# add_or_login()