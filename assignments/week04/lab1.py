"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies  #เพิ่มข้อมูลในlist
Remove hobbies
Update age (by creating a new tuple)

"""
# Complete this program
def personal_info_manager(): #defคือฟังช์ฟันในภาษาpython
    # Create initial person tuple
    person = ("Nichakamon: ", 19 , "Chonburi" , "TH")   # name, age, city, country
    hobbies = []

    while True:
        choice = input("Please select (1 display info, 2 add hobby, 3 remove hobby, 4 edit age,) ")
    
        # Your code here
        if choice == "1":
            #display info
            print("Name: ",person[0])
            print("Age:", person[1])
            print("City:", person[2])
            print("Conuntry:", person[3])
            print("Hobbies:", hobbies)

        elif choice == "2":
            #add hobby
            hobby = input("What is your hobby: ")
            hobbies.append(hobby)

        elif choice == "3":
            #remove hobby
            del hobbies[0]

        elif choice == "4":
            #edit ages
            person_list = list(person)
            age = int(input("How old are you?: "))
            person_list[1] = age
            person = tuple(person_list)

        elif choice == "5":
            break

if __name__ == "__main__":
    personal_info_manager()
    
   