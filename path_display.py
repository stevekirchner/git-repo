""" path_display """
import collections
import os

path = os.getenv('Path').lower().strip()

#remove blank entries
DOUBLE_SEPS = os.pathsep + os.pathsep
path = path.replace(DOUBLE_SEPS, os.pathsep)
    
path_list = path.split(os.pathsep)

# Remove any trailing os.sep characters
for i, item in enumerate(path_list):
    if item.endswith(os.sep):
        path_list[i] = item.strip(os.sep)

# Check for duplicates
duplicates = [item for item, count in collections.Counter(path_list).items() if count > 1]

sorted_list = sorted(set(path_list))

for item in sorted_list:
    if item in duplicates:
        print ( f'{item} is duplicated', end = "")
        if not os.path.exists(item):
            print ( " and does not exist" )
        else:
            print ( "" )
    elif os.path.exists(item):
        print(item)
    elif item == "": # Ignore empty string
        continue
    else:
        print(item + " does not exist")
