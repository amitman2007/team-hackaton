from tkinter import Label
import host
import hosted
import date
import description
import tkinter\
#


#
#
# root = tkinter.Tk()
# w = Label(root, text='GeeksForGeeks.org!')
# w.pack()
# root.mainloop()
#
#








# m.mainloop()





import login
from const import user_database


def main():
    username = False
    while username == False:
        username = login.add_or_login()
        if username != bool:
            description.create_info(username)


    guest_or_host=date.main_menu()
    print(guest_or_host)
    if guest_or_host=='guest':
        hosted.district_sort()
        hosted.date_of_party()
        hosted.event_sort()

    else:
        host.the_host()



main()
