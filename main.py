"""DA Points calculator
    Sam Goldberg"""

def main():
    print("Welcome to the DA Points Calculator!")
    print("\n")
    print("Would you like to convert TO Points or convert FROM Points?")
    print("Press 1 for TO Points and 2 for FROM Points")
    choice = input(">: ")
    if choice == "1":
        convert_to_points()
    if choice == "2":
        convert_to_dollars()
    else:
        print("Not Valid!")

def convert_to_points():
    print("PLease enter the dollar amount you would like to have converted to DA points")
    da_dollar = input(":: ")
    da_points = float(da_dollar)* .80
    print(f"{da_dollar} in DA points is {da_points:.2f}")

def convert_to_dollars():
    print("PLease enter the DA Points amount you would like to have converted to Dollars")
    da_points = input(":: ")
    da_dollar = float(da_points)* .80
    print(f"{da_points} DA Points in Dollars is {da_dollar:.2f}")


if __name__ == '__main__':main()