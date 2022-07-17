import sys
import clipboard
import json


# argv is a list in Python that contains all the command-line arguments passed to the script. 

#print(sys.argv[1:])

# if the length of arguments is 2 then printing the argument in the form of list that has index  position 1 i.e example:hello

SAVED_DATA = "multiclipboard.json"

def save_info(filepath,info):
    with open(filepath,"w") as f:
        json.dump(info,f)

#Loading or reading saved file as
def load_item(filepath):
    try:
        with open(filepath,"r") as f:
            info =json.load(f)
            return info
    except:
        return {}


if len(sys.argv)==2:
    data= sys.argv[1]
    info = load_item(SAVED_DATA)

# Used to save key and value pair

    if data == "save":
        key = input("Enter a key:")
        info[key] = clipboard.paste()
        save_info(SAVED_DATA,info)
        print("KEY SAVED SUCCESSFULLY!!")

    elif data == "load":
        key = input("Enter key:")
        if key in info:
            clipboard.copy(info[key])
            print("Info Copied Successfully!!")
        else:
            print("KEY DOESN'T EXISTS !!")

    elif data=="list":
        print(info)

    else:
        print("Unknown Command!!")

else:
    print("PLEASE ENTER ONE COMMAND AT A TIME!!")
    




    




 