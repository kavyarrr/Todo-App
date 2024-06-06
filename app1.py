import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
while True:
   act=input("Type add, exit,edit,complete or show: ")
   act=act.lower().strip()
   if act.startswith("add"):
       todo=act[4:] + "\n"
       todos=functions.call()

       todos.append(todo)

       functions.change(todos)
   elif act.startswith("show"):
       todos=functions.call()

       # todos=[i.strip() for i in todos]

       for index,item in enumerate(todos): #gives index as well as element
           print(f"{index+1}-{item.strip().title()}")
   elif act.startswith("exit"):
       break
   elif act.startswith("edit"):
       try:
           todos=functions.call()

           n=int(act[5:])
           new=input("enter new todo")
           todos[n-1]=new + "\n"

           functions.change(todos)
       except (ValueError,IndexError):
           print("Your command is not valid")
           continue

   elif act.startswith("complete"):
       try:
           todos=functions.call()

           n=int(act[9:])
           print(f"Todo '{todos[n-1].strip().title()}' was removed from list")
           todos.pop(n-1)

           functions.change(todos)
       except IndexError:
           print("There is no item with that number")
           continue
   else:
       print("Invalid command. Try again.")
print("bye!")
