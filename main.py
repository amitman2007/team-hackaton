import description


















import login
from const import user_database
username=False
while username==False:
    username=login.add_or_login()

    if username != bool:
        description.create_info(username)
        print(description.text)




