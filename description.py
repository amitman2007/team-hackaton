import login
text={'afik':'ani aohev banim im zain'}
def create_info(username):
    info=''
    age=input("enter your age")
    living=input("where do you live ")
    work=input("what do you do for living?")
    hobbies=input("what are your hobbies:")
    general_info=input("fun fact about yourself :)")
    info=age+' '+living+work+' '+hobbies+' '+general_info
    text[username]=info
    return text


