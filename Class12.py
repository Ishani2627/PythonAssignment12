#Que1
print("print current day")
import datetime
now = datetime.datetime.now()
print("current day : ", now.day)

#Que2
print("play a video using web browser")
import webbrowser
play = 1
webbrowser.open("https://www.youtube.com/watch?v=iSallxKpm8Y", new = play)

#Que3
print("rename files and convert into .jpg")
import os
path = '/Users/Ishani/Desktop/PythonAssignments/PythonAssignment12/files'
files = os.listdir(path)
i = 1
for file in files:
    os.rename(os.path.join(path,file), os.path.join(path,str(i)+'.jpg'))
    i = i+1
print(".png files are converted to .jpg")