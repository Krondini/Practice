def main():
    objects = {}
    while(True):

        new_obj = input("Would you like to enter a new object? [Y/n]")
        if new_obj.lower() == 'y':
            obj_name = input("Please enter the name of your object: ").lower()
            obj_loc = input("Please enter the location of your object: ").lower()
            objects[obj_name] = obj_loc

        elif new_obj.lower() == 'n':
            print("Exiting program.")
            return objects

        else:
            print("Invalid input, please try again.")

if __name__ == '__main__':
    objects = main()
    f = open("output.txt", 'w')
    f.write(str(objects))