hosted_list=[]


events_list={'1':"holiday eve", '2':"lodging", '3':"visit elderly people",'4':"happy events"}



def event_sort():
    print("what : ", events_list)

    choosen_event=input("please enter the number of your event(1-4):")
    for i in range(len(events_list)):
        if choosen_event == events_list[i]:
            hosted_list.append(events_list[i])
            # print(hosted_list)



def date_of_party():
    date_of_event=input("enter the date:")
    hosted_list.append(date_of_event)


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







