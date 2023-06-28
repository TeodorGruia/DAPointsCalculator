"""DA Points calculator
    Sam Goldberg"""

def main():
    print("Welcome to the DA Points Calculator!")
    print("\n")
    print("PLease enter the dollar amount you would like to have converted to DA points")
    da_dollar = input(":: ")
    da_points = float(da_dollar)* .80
    print(f"{da_dollar} in DA points is {da_points:.2f}")

def convert_to_points():
    pass
def convert_to_dollars():
    pass

if __name__ == '__main__':main()