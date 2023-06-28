"""DA Points calculator
    Sam Goldberg"""

def main():
    print("Welcome to the DA Points Calculator!")
    menu()
    choice = input(">: ")
    if choice == "1":
        convert_to_points()
    if choice == "2":
        convert_to_dollars()
    if choice == "q":
        exit()
def menu():
    print("--Conversion Menu--")
    print("Please select 1 or 2 or q to quit")
    print("USD to DA Points: 1")
    print("DA Points to USD: 2")
    print("Quit: q")

def convert_to_points():
    print("Dollars to DA Points")
    print("Please enter the dollar amount you would like to have converted to DA points")
    da_dollar = input(":: ")
    da_points = float(da_dollar)* 80
    print(f"{da_dollar} in DA points is {da_points:.2f}")
    go_again()

def convert_to_dollars():
    print("DA Points to Dollars")
    print("Please enter the DA Points amount you would like to have converted to Dollars")
    da_points = input(":: ")
    da_dollar = float(da_points)/ 80
    print(f"{da_points} DA Points in Dollars is {da_dollar:.2f}")
    go_again()

def go_again():
    print("Do you want to convert again?")
    print("y: yes n: no")
    choice = input(">:")
    if choice == "y":
        main()
    if choice == "n":
        exit()

if __name__ == '__main__':main()