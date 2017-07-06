# the key of the dictionary is the ID of the person
# inside the university
db_university = { "1AEF" : {
    "first_name": "Christian",
    "last_name": "Barra",
    "status" : "Active",
    "role": "Student"
    },
    "2BED" : {
    "first_name": "Jolanta",
    "last_name": "Pizza",
    "status" : "Inactive",
    "role": "Student"
    },
    "2BEC" : {
    "first_name": "Wioletta",
    "last_name": "",
    "status" : "Inactive",
    "role": "Student"
    },
    "4AEF" : {
    "first_name": "Michal",
    "last_name": "Bojano",
    "status" : "Active",
    "role": "Professor",
    "students": ["1AEF", "2BED"]
    },
    "8ACF" : {
    "first_name": "Salvatore",
    "last_name": "Pedalino",
    "status" : "Inactive",
    "role": "Professor",
    "students": []
    }}

#print (help(db_university))
def api_call(db, person_id):
    '''This function takes a dict object and a id (unique identifier)
        then the function should return:

        If the id is of a student a list with 3 elements ["first_name", "last_name", "status"]
        If it's a professor a list with 4 elements ["first_name", "last_name", "status", [d_list] ]

        the 4th element is a list of dictionaries where each dict contains {"name": name, "id" : id}
        :name is a string with the fist and last name "Chritian Barra"
        :id is the id of that person "1AEF" in my case
        the list must contain a dict for each student, and should be empty in case it has no students

        '''
    # checking the id if it is in the DB
    if person_id in db:
        if db[person_id]['role'] == 'Student':
            #return [db[person_id]]["first name"],{}
            first_name = db[person_id]['first_name']
            last_name = db[person_id]['last_name']
            status = db[person_id]['status']
            return [first_name, last_name, status]
        elif db[person_id]['role'] == 'Professor':
                # return [db[person_id]]["first name"],{}
            first_name = db[person_id]['first_name']
            last_name = db[person_id]['last_name']
            status = db[person_id]['status']
            students =[]
            for student_id in db[person_id]['students']:
                s_first_name = db[student_id]['first_name']
                s_last_name = db[student_id]['last_name']


                name = f"{s_first_name} {s_last_name}"
                students.append({"name":name, "id":student_id})
                return [first_name, last_name, status, students]
    else:
        print ("Your DB doesn't have the key")
print(api_call(db_university, "8AF"))
    #if dict_object[id_inside_db]: "role"
    #dict_object[]

    # put your code here
    # leave the rest
