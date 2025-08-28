from hosted import district, events_list

all_host_list = []
host_list={}

def the_host():
    name_of_event = input("please enter your name of event:")
    events_list={'1':"holiday", '2':"kiddush", '3':"meetup",'4':"other events"}
    print("choose which event you would like to host?: ", events_list)


    chosen_event=events_list[input("please enter the number of the event(1-4):")]
    date_of_event=input("enter the date:")
    district = {
            '1':"jerusalem district", '2':"northern district ", '3':"haifa district",
                '4':"central district", '5':"south district", '6':"west district"

    }
    print(" chose your district from the list: ", district)

    chosen_district = district[input("please enter the num of the district(1-6):")]
    hour_of_event=input("enter the hour:")


    host_list["name_of_event"]=name_of_event
    host_list["chosen event"]=chosen_event
    host_list["date of event"]=date_of_event
    host_list["chosen district"]=chosen_district
    host_list["hour of event"]=hour_of_event
    all_host_list.append(host_list)



    print("CONGRATULATIONS!!!!!! YOUR EVENT HAS BEEN NOTED , THE INVENTIONS HAS BEEN SEND ")
    print(all_host_list)

