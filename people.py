import random
people_list=[]
people_dict={}
def rand_people():
   people_list=[]
   people_dict={}
   for i in range(100):
    username=(f"person{i+1}")
    events_list_choice =  ["holiday", "kiddush",  "meetup",  "other events"]
    district_choice = ["jerusalem district",  "northern district ",  "haifa district",
     "central district", "south district", "west district"]
    event= random.choice(0,3)
    living=random.choice(0,5)

    people_list.append(events_list_choice[event],district_choice[living])
    people_dict[username]=people_list
   return people_dict
   print(rand_people())


rand_people()
