import functions as fun
import FreeSimpleGUI as fsg
label=fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo",key="Todo")
add_button = fsg.Button("Add")
window = fsg.Window('My To-Do App',
                    layout=[[label],[input_box,add_button]],
                    font=("Helvetica",13))
while True:
    eve,val=window.read()
    print(eve,"|",val)
    match eve:
        case "Add":
            todos= fun.call()
            newtodo=val['Todo'] + "\n"
            todos.append(newtodo)
            fun.change(todos)
        case fsg.WIN_CLOSED:
            break
window.close()