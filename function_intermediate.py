# Change the value 10 in x to 15. 
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# # print(students[0]['last_name'])
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

# # print(sports_directory['soccer'][0])
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])


# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

# print(z[0]['y'])
z[0]['y'] = '30'
print(z[0]['y'])


# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionary(lst):
    for i in range(0,len(lst), 1):
        # print(lst[i])
        str = ""
        for key, value in lst[i].items():
            str += key + " - " + value + ", "
            # print(f"{lst[i]['first_name']},- {lst[i]['last_name']}")
        print(str)
print(students)



iterateDictionary(students) 
# # # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # # bonus to get them to appear exactly as below!)
# # # first_name - Michael, last_name - Jordan
# # # first_name - John, last_name - Rosales
# # # first_name - Mark, last_name - Guillen
# # # first_name - KB, last_name - Tonel





# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(len(some_dict["locations"]),"LOCATIONS")
    for location in some_dict["locations"]:
        print(location)

    print(len(some_dict["instructors"]),"INSTRUCTORS")
    for location in some_dict["instructors"]:
        print(location)



printInfo(dojo)
# # # # output:
# # # 7 LOCATIONS
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank

# # 8 INSTRUCTORS
# # Michael
# # Amy
# # Eduardo
# # Josh
# # Graham
# # Patrick
# # Minh
# # Devon




















