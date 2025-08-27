hosted_list=[]


# events_list=["holiday eve", "lodging", "visit elderly people","happy events"]
# print("welcome to de website our events: ", events_list)
#
#
# def event_sort():
#
#     choosen_event=input("please enter your event:")
#     for i in range(len(events_list)):
#         if choosen_event == events_list[i]:
#             hosted_list.append(choosen_event)
#             print("searching events for you by name:",events_list[i])
#             # print(hosted_list)
# event_sort()
#
# date_of_event=input("enter the date:")
# hosted_list.append(date_of_event)


def district_sort ():
    district = ["jerusalem district", "northern district ", "haifa district", "central district", "south district",
                "west district"]
    chosen_district = input("please enter the district:")
    for i in range(len(district)):
        if chosen_district == district[i]:
            hosted_list.append(chosen_district)
            print("searching events for you by name:", chosen_district[i])
            print(hosted_list)
district_sort()

# print(hosted_list)
