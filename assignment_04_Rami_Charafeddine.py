def getSumTuples():
    # two inputs 
    input1 = input("Enter numbers separated by #: ")
    input2 = input("Enter numbers separated by #: ")

    # convert to lists
    list1 = input1.split("#")
    list2 = input2.split("#")
    list3 = []  # create list

    #sum elements in loop
    for i in range(len(list1)):
        sum_value = int(list1[i]) + int(list2[i])
        list3.append(sum_value)

    # convert to tuple
    tuple_3 = tuple(list3)
    print("Sum of tuples:", tuple_3)
    return tuple_3


def exportJSON(dictionary, filename):
    with open(filename, 'w') as file:
        file.write('{\n')  #opening brace for json

        keys = list(dictionary.keys())  #make keys list to do for loop
        len_keys = len(keys)    

        for i in range(len_keys):  # Loop through each key-value pair
            key = keys[i]
            value = dictionary[key]

            file.write(f' "{key}": ')  #wrap key in double quotes and write it

            #value type handling:
            if value == True:         # check if value boolean
                file.write("true")
            elif value == False:
                file.write("false")
            elif type(value) == list:   #check if list
                file.write("[")   #open list

                for j in range(len(value)):  #convert each element to str
                    file.write(str(value[j]))  #add commas
                    if j < len(value) - 1:
                        file.write(", ")
                
                file.write("]")   #close list
            
            else:   #if numb or str
                try:
                    file.write(str(int(value)))  #check if value int
                except ValueError:
                    file.write(f' "{value}" ')   #else convert to str

            if i < len_keys - 1:    #add comma after key-value
                file.write(",\n")
        
        file.write("\n}")   #close json 

    print("Dictionary exported to", filename)


def importJSON(filename):
    with open(filename,'r') as file:  #open file
        content = file.read()   #read file

        if content.startswith("{") and content.endswith("}"): 
            content = content[1:-1].strip()   #check if json/remove braces
        else:
            print("Invalid json format")

        pairs = content.split(", ")   #create list key-value pairs
        new_dict = {}   #initialize dictionary

        for pair in pairs:
            key_value = pair.split(":", 1)   #split at first colon
            if len(key_value) != 2:
                print("Invalid pair", pair)  #skip invalid pairs
                continue

            key = key_value[0].strip().strip('"')   #clean up key
            value = key_value[1].strip()    #clean up value

            #check data type
            if value == "true":
                new_dict[key] = True
            elif value == "false":
                new_dict[key] = False
            elif value.isdigit():
                new_dict[key] = int(value)  #convert to int
            else:
                try:
                    new_dict[key] = float(value)  #convert to float
                except ValueError:
                    new_dict[key] = value.strip('"')  #keep as str

    return new_dict 


# menu loop
def menu():
    while True:
      
        print("\n--- Menu ---")
        print("1. Sum Tuples")
        print("2. Export JSON")
        print("3. Import JSON")
        print("4. Exit")

        choice = input("Choose your character: ")

        if choice == "1":  
            getSumTuples()


        elif choice == "2":  
            dictionary = {
                "fname": "Johnny",
                "lname": "Alawieh",
                "age": 101,
                "is_alive": True,
                "kids": ["baby1", "baby2"],
                "kids_age": [4, 2]
            }

            filename = input("Enter filename to export JSON: ")
            exportJSON(dictionary, filename)


        elif choice == "3":  
            filename = input("enter filename to import JSON: ")
            new_dict = importJSON(filename)
            print("imported JSON as dictionary:", new_dict)


        elif choice == "4": 
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")



menu()

#Ex2:
# a:O(n^3)

# b:O(n^3)

# c:O(n!)
  
# d:O(nlogn)

# e:O(n)

# f:O(n^2)

# g:O(n^2)

# h:O(n!)


