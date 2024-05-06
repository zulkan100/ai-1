# def add_task(tasks, new_task):
#     tasks.append(new_task)
#     print("Task added successfully!")

# def view_tasks(tasks):
#     if not tasks:
#         print("No tasks in the list.")
#     else:
#         print("To-Do List:")
#         for index, task in enumerate(tasks, start=1):
#             print(f"{index}. {task}")

# def mark_completed(tasks, task_index):
#     if 1 <= task_index <= len(tasks):
#         completed_task = tasks.pop(task_index - 1)
#         print(f"Task '{completed_task}' marked as completed.")
#     else:
#         print("Invalid task index.")

# def main():
#     tasks = []

#     while True:
#         print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             new_task = input("Enter the task: ")
#             add_task(tasks, new_task)
#         elif choice == '2':
#             view_tasks(tasks)
#         elif choice == '3':
#             view_tasks(tasks)
#             task_index = int(input("Enter the task index to mark as completed: "))
#             mark_completed(tasks, task_index)
#         elif choice == '4':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please try again.")

def addMenu(menu, addOrder):
  menu.append(addOrder)
  print("Food ordered Successfully")

def viewOrder(menu):
  if not menu:
    print("No foods ordered")
  else:
    print("--Foods Ordered--")
    for i in range(len(menu)):
      print(f"{i+1}. {menu[i]}")

def viewMenu(bigMenu):
  print("--Alepa's Fast food--")
  for i in range(len(bigMenu)):
    print(f"{i+1}. {bigMenu[i]}")

menu =[]
bigMenu = ["Burger", "Pizza", "Noodles", "Coca Cola", "Pepsi", "Chicken", "Pork"]

while True:
  print("\n1. Add Order\n2. View Orders\n3. Look at Menu\n4. Exit")
  choice = input("Enter your choice: ")
  if choice == '1':
    addOrder = input("Enter the food: ")
    addMenu(menu, addOrder)
      
  elif choice == '2':
    viewOrder(menu)
  
  elif choice =="3":
    viewMenu(bigMenu)
  elif choice =="4":
    break
