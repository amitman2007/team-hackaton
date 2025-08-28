all_host_list = []
host_list={}

def the_host():
    name_of_event = input("please enter your name of event:")
    events_list={"holiday eve":1, "lodging":2, "visit elderly people":3,"happy events":4}
    print("welcome to de website our events: ", events_list)


    chosen_event=input("please enter the number of the event(1-4):")
    date_of_event=input("enter the date:")
    district = {
            "jerusalem district":1, "northern district ":2, "haifa district":3,
                "central district":4, "south district":5, "west district":6

    }
    print(" chose your district from the list: ", district)

    chosen_district = input("please enter the num of the district(1-6):")
    hour_of_event=input("enter the hour:")


    host_list["name_of_event"]=name_of_event
    host_list["chosen event"]=chosen_event
    host_list["date of event"]=date_of_event
    host_list["chosen district"]=chosen_district
    host_list["hour of event"]=hour_of_event
    all_host_list.append(host_list)



    print("CONGRATULATIONS!!!!!! YOUR EVENT HAS BEEN NOTED , THE INVENTIONS HAS BEEN SENT ")
    print(all_host_list)

the_host()
