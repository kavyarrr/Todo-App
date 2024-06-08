import functions
import FreeSimpleGUI as fsg
label=fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo")
add_button = fsg.Button("Add")
window = fsg.Window('My To-Do App',layout=[[label],[input_box,add_button]]) #window instance
window.read()
window.close()