import functions as fun
import FreeSimpleGUI as fsg
import time as t
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as f:
        pass

fsg.theme("DarkPurple4")
timelabel=fsg.Text('',key="clock")
label=fsg.Text("Type in a to-do")
add_button = fsg.Button("Add")
input_box = fsg.InputText(tooltip="Enter todo",key="Todo")

edit_button= fsg.Button("Edit")
list= fsg.Listbox(values=fun.call(),key="todos",
                  enable_events=True,size=[45,10])

exit_button=fsg.Button("Exit")
comp_button=fsg.Button("Complete")
window = fsg.Window('My To-Do App',
                    layout=[[timelabel],[label],[input_box,add_button],
                            [list, edit_button,comp_button],
                            [exit_button]],
                            font=("Helvetica",13))
while True:
    eve,val=window.read(timeout=200)
    window["clock"].update(value=t.strftime("%b %d, %H:%M:%S"))
    # print(eve)
    # print(val)
    match eve:
        case "Add":
            todos= fun.call()
            newtodo=val['Todo'] + "\n"
            todos.append(newtodo)
            fun.change(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_edit=val["todos"][0] #the todo they want to edit
                newtodo= val["Todo"] + "\n"
                todos=fun.call()
                index=todos.index(todo_edit)
                todos[index]=newtodo
                fun.change(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select item first",font=("Helvetica",20))
        case "Complete":
            try:
                todo_comp=val["todos"][0]
                todos=fun.call()
                todos.remove(todo_comp)
                fun.change(todos)
                window['todos'].update(values=todos)
                window["Todo"].update(value='')
            except IndexError:
                fsg.popup("Please select item first", font=("Helvetica", 20))
        case 'todos':
            window['Todo'].update(value=val['todos'][0])
        case fsg.WIN_CLOSED:
            break
        case "Exit":
            break
window.close()
