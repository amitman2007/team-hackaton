all_host_list = []
host_list={}


name_of_event = input("please enter your name of event:")
chosen_event=input("please enter your event:")
date_of_event=input("enter the date:")
chosen_district = input("please enter the district:")
hour_of_event=input("enter the hour:")


host_list["name_of_event"]=name_of_event
host_list["chosen event"]=chosen_event
host_list["date of event"]=date_of_event
host_list["chosen district"]=chosen_district
host_list["hour of event"]=hour_of_event
all_host_list.append(host_list)



print("CONGRATULATIONS!!!!!! YOUR EVENT HAS BEEN NOTED , THE INVENTIONS HAS BEEN SEND ")
print(all_host_list)
