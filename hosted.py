hosted_list=[]


events_list={"holiday eve":1, "lodging":2, "visit elderly people":3,"happy events":4}
print("welcome to de website our events: ", events_list)


def event_sort():

    choosen_event=input("please enter the number of your event(1-4):")
    for i in range(len(events_list)):
        if choosen_event == events_list[i]:
            hosted_list.append(events_list[i])
            # print(hosted_list)
event_sort()



def date_of_party():
    date_of_event=input("enter the date:")
    hosted_list.append(date_of_event)

date_of_party()

district = {
        "jerusalem district":1, "northern district ":2, "haifa district":3,
            "central district":4, "south district":5, "west district":6

}
print(" chose your district from the list: ", district)

def district_sort ():

    chosen_district = input("please enter the number of the chosen district(1-6):")
    for i in range(len(district)):
        if chosen_district == district[i]:
            hosted_list.append(district[i])
            print(hosted_list)
district_sort()







