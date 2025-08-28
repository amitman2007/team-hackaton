hosted_list=[]


events_list={'1':"holiday eve", '2':"lodging", '3':"visit elderly people","happy events":4}
print("choose activity: ", events_list)


def event_sort():

    choosen_event=input("please enter the number of your event(1-4):")
    for i in range(len(events_list)):
        if choosen_event == events_list[choosen_event]:
            hosted_list.append(events_list[i])

event_sort()



def date_of_party():
    date_of_event=input("enter the date:")
    hosted_list.append(date_of_event)

date_of_party()

district = {
        '1':"jerusalem district", '2':"northern district", '3':"haifa district",
            '4':"central district", '5':"south district", '6':"west district"
}
print(" chose your district from the list: ", district)

def district_sort ():

    chosen_district = input("please enter the number of the chosen district(1-6):")
    for i in range(len(district)):
        if chosen_district == district[i]:
            hosted_list.append(district[i])
            print(hosted_list)
district_sort()







