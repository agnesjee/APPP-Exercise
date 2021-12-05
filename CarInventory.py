
#### Libraries ####

# For generating dataframe
import pandas as pd

# For graph plotting
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10,8)})

# For counting elements
from collections import Counter

# Creating a dictionary "carDic"
carDic = {}



#### Classes ####
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
 
    

#### Functions ####
def addCar(name, kind, color, value):
    car = Vehicle()
    car.name = name
    car.kind = kind
    car.color = color
    car.value = value 
    print(car.description())
    
    carDic[car.name] = [car.name, car.kind, car.color, car.value]
    print("Successfully added.")
    
    
    
def editCar(edit_name):
    if edit_name in carDic:
        print("Details of " + edit_name + ": ")
        print(carDic[edit_name])
        
        print("Please enter the new data:")
        updatedName = input("Enter car name: ")
        updatedKind = input("Enter car kind: ")
        updatedColor = input("Enter car color: ")
        updatedValue = float(input("Enter car value: "))
        
        # Change the name of the key to a new one first
        carDic[updatedName] = carDic.pop(edit_name)
        carDic[updatedName] = [updatedName, updatedKind, updatedColor, updatedValue]
         
        print("Successfully updated.")
        
    else:
        print("The car does not exist in the dictionary.")
        
        
    
def deleteCar(delete_name):
    if delete_name in carDic:
        del carDic[delete_name]
        print("Successfully deleted.")

    else:
        print("The car does not exist in the dictionary.")



def displayCar():
    if(len(carDic) == 0):
        print("\nThere is no car being added yet.")
    else:
        dicItems = carDic.items()
        for item in dicItems:
            print(item)
    


def visualizeCar():
    df = pd.DataFrame(carDic, index=['Car Name', 'Car Kind', 'Car Color', 'Car Value'])
    print("Car Info in Table Form:")
    print(df)
    print("\n")
    
    # Extract the car kind in each car 
    subset = df.loc["Car Kind"]
    print(subset)
    print("\n")
    
    # Get the frequency of each car kind
    counts = Counter(subset)
    print(counts)
    
    # Plot the graph
    plt.bar(counts.keys(), counts.values())
    plt.show()
    
    
    
def saveFile():
    file = open("carRecords.txt", "w")
    records = str(carDic)
    file.write(records)
    file.close()

    print("Successfully saved.")

    
#### Main Body ####

while True: 
    print("\n")
    print("========")
    print("Welcome to Second-Hand Car Dealer! What would you like to start with?")
    print("========")
    choice = int(input("1. Add New Cars\n2. Edit Car Records\n3. Delete Car Records\n4. Display Car Records\n5. Show data visualization of the car records\n6. Save the file\n7. Exit the program\nYour choice: "))
    print("\n")
    
    if (choice == 1):
        name = input("Enter car name: ")
        kind = input("Enter car kind: ")
        color = input("Enter car color: ")
        value = float(input("Enter car value: "))
        print("\n")
        
        addCar(name, kind, color, value)
        
    elif (choice == 2): 
        edit_name = input("Enter the name of the car you want to edit: ")
        editCar(edit_name)
        
    elif (choice == 3):
        delete_name = input("Enter the name of the car you want to delete: ")
        deleteCar(delete_name)
        
    elif (choice == 4):
        displayCar()
        
    elif (choice == 5):
        visualizeCar()
        
    elif (choice == 6):
        saveFile()
        
    elif (choice == 7):
        print("Thank you for using our service! See you next time.")
        break
    
    else:
        print("\nPlease select a valid option.")








