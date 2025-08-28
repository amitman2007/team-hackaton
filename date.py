
def main_menu():
    action_manu=''
    while action_manu != '1' and action_manu != '2':
        action_manu=input('do you want to be a guest(enter 1) or a host(enter 2)?')
    if action_manu == "1":
        return "guest"
    else:
        return "host"
