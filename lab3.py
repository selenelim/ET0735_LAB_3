print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print("get_user_input")
    inputstr = input()   # Read the number sequence entered by user.
    
    # Separate the numbers sequence into short strings, using the split() function
    strlist = inputstr.split(",")
    print("After split:", strlist)

    # Convert every element in the strlist from string to float.
    floatlist = []    # Create an empty list
    for eachstr in strlist:
        floatlist.append(float(eachstr))   # Append element to the floatlist
    print("Data List:", floatlist)
    return floatlist


def calc_average(datalist):
    print("calc_average")
    total = 0.0
    for eachData in datalist:
        total = total + eachData
    # The two lines above can be replaced by
    # total = sum(datalist)
    average = total / len(datalist)
    print("Average = ", average)
    return average


def find_min_max(datalist):
    print("find_min_max")

    # The sort() function alters the list. In order
    # not to corrupt the datalist, make a copy of it,
    # and do the sorting on the copy.
    floatlist = datalist.copy()   # make a copy
    floatlist.sort()
    print("MIN = ", floatlist[0])
    print("MAX = ", floatlist[-1])
    return (floatlist[0], floatlist[-1])



def sort_temperature():
    print("sort_temperature")


def calc_median_temperature():
    print("calc_median_temperature")



def main():
    print("*** ET0735 Lab 2 Ex3")
    display_main_menu()
    resultlist = get_user_input()

    avg = calc_average(resultlist)
    print("*** Average is ", avg)

    minimum, maximum = find_min_max(resultlist)
    print("*** Minimum is ", minimum)
    print("*** Maximum is ", maximum)

    print("*** End of program")



if __name__ == "__main__":
    main()
