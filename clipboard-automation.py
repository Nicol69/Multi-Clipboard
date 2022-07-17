import sys
import clipboard
import json


# argv is a list in Python that contains all the command-line arguments passed to the script. 

#print(sys.argv[1:])

# if the length of arguments is 2 then printing the argument in the form of list that has index  position 1 i.e example:hello
def save_info(filepath,info):
    with open(filepath,"w") as f:
        json.dump(info,f)
save_info("testing.json",{"employee":"paid"})


if len(sys.argv)==2:
    data= sys.argv[1]
    if data == "save":
        print("Saved")
    elif data == "load":
        print("Loaded")
    elif data=="list":
        print("Listed")
    else:
        print("Unknown command")
else:
    print("Command length must not exceed 2")
    




    




 