import functions as fun
import FreeSimpleGUI as fsg
label=fsg.Text("Type in a to-do")
add_button = fsg.Button("Add")
input_box = fsg.InputText(tooltip="Enter todo",key="Todo")

edit_button= fsg.Button("Edit")
list= fsg.Listbox(values=fun.call(),key="todos",
                  enable_events=True,size=[45,10])

window = fsg.Window('My To-Do App',
                    layout=[[label],[input_box,add_button],[list, edit_button]],
                    font=("Helvetica",13))
while True:
    eve,val=window.read()
    print(eve)
    print(val)
    match eve:
        case "Add":
            todos= fun.call()
            newtodo=val['Todo'] + "\n"
            todos.append(newtodo)
            fun.change(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_edit=val["todos"][0] #the todo they want to edit
            newtodo= val["Todo"] + "\n"
            todos=fun.call()
            index=todos.index(todo_edit)
            todos[index]=newtodo
            fun.change(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['Todo'].update(value=val['todos'][0])
        case fsg.WIN_CLOSED:
            break
window.close()