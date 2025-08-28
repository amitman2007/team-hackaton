import random
import copy
from const import user_database

people_list=[]
people_dict={}
events_list_choice =  ["holiday", "kiddush",  "meetup",  "other events"]
district_choice = ["jerusalem district",  "northern district ",  "haifa district",
                   "central district", "south district", "west district"]
user_to_add=[]
def rand_people():
   people_list=[]
   people_dict={}
   for i in range(100):
       username = (f"person{i + 1}")

       event = random.randrange(0, 3)
       living = random.randrange(0, 5)

       user_to_add.append(events_list_choice[event])
       user_to_add.append(district_choice[living])

       people_dict[username] = copy.deepcopy(user_to_add)
       user_to_add.clear()
   return people_dict

print(rand_people())


