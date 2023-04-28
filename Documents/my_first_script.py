def find_fav():
    print("Who is your favorite QC team member?")
    name = input()
    name = name.upper()
    
    return(name)

name = find_fav()
while name != "ZACH":
    print("Try again.....")
    name = find_fav()
    
print("Correct! Thank you for playing.")
