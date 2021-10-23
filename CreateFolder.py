# script that creates a new directory of a given name in the folder above folder, referencing the latter with the created environment variable

#Import Modules
import os

#Import Env Variables
Research_Path=os.environ.get('RESEARCH_PATH')

#Promt Name for new directory 
new_project= input("Enter name for new directory: ")

#Create dir in Reseach PathFolder
os.mkdir(Research_Path + "/" + new_project)

print(new_project+"has been created")



#### more info/code
#path = os.getcwd()
#print ("The current working directory is %s" % path)


