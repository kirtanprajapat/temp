# import 
from enum import Enum

task = {}

class status(Enum):
    Done = True
    Pending = False


def task_view():
    a = task.items()
    print (list(a))

def task_add():
    q = int(input("How many task you want to enter: "))
    for i in range(q):
         key = input("Enter key: ")
         value = input("Enter value (Done or Pending): ")
         if(value == "Done"):
             enum_value = status.Done

         elif(value == "Pending"):
             enum_value = status.Pending

         else:
             break
    task[key] = enum_value
    

print("Task menu \n")
print("To View Tasks Press 1:")
print("To Add Tasks Press 2:")
print("To Edit Tasks Press 3:")
print("To Delete Tasks Press 4:")

b = int(input("Enter the number:"))
if(b==1):
    task_view()
elif(b==2):
    task_add()
    task_view()
