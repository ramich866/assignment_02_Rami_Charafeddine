def countDigits(integer):
    
    if integer < 0:
        integer = -integer    #converts to pos if neg

    if integer == 0:  #base case
        return 0      # return 0 to avoid counting it  

    else: 
        return 1 + countDigits(integer//10) 
            #recursively counting by dividing the integer
def findMax(lst):
    if not lst:     #if list empty
        return 0

    if len(lst) == 1:   #base case one element
        return lst[0]

    max_num = findMax(lst[1:])  #recursive, find the max in the rest

    return lst[0] if lst[0] > max_num else max_num 
    #compare first element with max of the rest
def countTags(html, tag):

    open_tag = f"<{tag}>"   #creating variables
    close_tag = f"</{tag}>"

    start_index = html.find(open_tag)   #find open tag

    if start_index == -1:       #base case: no more start indexes
        return 0

    end_index = html.find(close_tag, start_index)   #find close tag 

    if end_index != -1:     #confirmation
        return 1 + countTags(html[end_index + len(close_tag):], tag)

    return 0


def main():

    choice = 0          #create variable

    while choice != 4:
        print("1. Count Digits\n2. Find Max\n3. Count Tags\n 4. Exit\n")

        try:       #input validation (prevents crashes)
            choice = int(input("Choose your character:"))

        except ValueError:
            print("Invalid. Try again")
            continue

        if choice == 1: 
            try:               
                integer = int(input("Enter an integer:"))
                print("The number of digits is:", countDigits(integer))

            except ValueError :
                print("Invalid. Try again")

            print("Choose again:\n")  #show menu again


        elif choice == 2:
            try:
                user_list = input("Enter a list of integers(e.g: 2, 9, -3):")

                lst = list(map(int, user_list.split(',')))

                print("the max value is", findMax(lst))

            except ValueError:
                print("Invalid input. Try again")

            print("Choose again:\n") 


        elif choice == 3:

            html_code = """
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>
"""

            tag = input("Enter the tag to count:")

            print(f"the tag <{tag}> appears {countTags(html_code, tag)} times")



        elif choice == 4:
            print("Exiting")



        else:
            print("Invalid number. Try again")



    print("Ahla w sahla")



main()

