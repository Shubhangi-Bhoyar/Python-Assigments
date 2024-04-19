
print("Welcome to the Certifictaion Database")
details = []
emp = {}
while True:
 print("Select your Operation ")
 print("1.Add New Record")
 print("2.Get Record")
 o = int(input())
 match o:
    case 1:
         print("Provide your details: Name, Certification, Level on a scale 1-10")
         a = (input("Name: "))
         if not a.isalpha():
            print("Provide textual data only")
            break
         b = (input("Certification: "))
         if not b.isalpha():
            print("Provide textual data only")
            break
         c = int(input("Level (on a scale of 1-10): "))
         if c == 0:
            print("level is between 1-10")
            break
         elif c > 10:
            print("Level is greater than 10")
            break

         details.append({"Name": a, "Certification": b, "Level": c})
         print(details)
    case 2:
      input1 = input("Search Name: ")
      for empdetails in  details:
            if empdetails["Name"] == input1:
                print("here are the details", empdetails)
    case _:
        print("Incorrect Operation")
        # exit(1)
