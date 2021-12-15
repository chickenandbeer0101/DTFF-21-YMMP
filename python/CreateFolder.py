# script that creates a new directory of a given name in the folder above folder, referencing the latter with the created environment variable

#Import Modules
import os

#Import Env Variables
RESEARCH_PATH=os.environ.get('RESEARCH_PATH')

def CreateFolder(new_project):
    #Promt Name for new directory 
    new_project= input("Enter name for new directory: ")

    #Create dir in Reseach PathFolder
    os.mkdir(RESEARCH_PATH + "/" + new_project)

    print(new_project+"has been created")



#### more info/code
#path = os.getcwd()
#print ("The current working directory is %s" % path)


