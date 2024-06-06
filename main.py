# import glob
# myfiles=glob.glob("files/*.txt")
# for f in myfiles:
#     with open(f,'r') as file:
#         print(file.read())

import webbrowser
u=input("enter search term ")
webbrowser.open("https://www.google.com/search?q="+ u)
