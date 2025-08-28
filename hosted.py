hosted_list=[]


events_list={'1':"holiday", '2':"kiddush", '3':"meetup","other events":4}
print("choose activity: ", events_list)


def event_sort():

    choosen_event=input("please enter the number of your event(1-4):")
    for i in range(len(events_list)):
        if choosen_event == events_list[choosen_event]:
            hosted_list.append(events_list[i])

event_sort()




district = {
        '1':"jerusalem district", '2':"northern district", '3':"haifa district",
            '4':"central district", '5':"south district", '6':"west district"
}


def district_sort ():
    print(" chose your district from the list: ", district)

    chosen_district = input("please enter the number of the chosen district(1-6):")
    for i in range(len(district)):
        if chosen_district == district[i]:
            hosted_list.append(district[i])
            print(hosted_list)







