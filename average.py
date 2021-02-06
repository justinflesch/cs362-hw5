# Cube program

def avg_list(items):
    value = 0
    value = float(value)
    if len(items) > 0:
        for i in items:
            try:
                value = value + float(i)
            except:
                print("Error: Invalid value passed")
                return
        value = value / len(items)
        return value
    else:
        print("Error: Zero values in list")
        return

class avg:
    def __init__(self):
        items = list()
        print("Enter nums for your array, type 'end' to get the average of that list: ")
        while(1):
            num1 = input("Enter a value: ")
            if num1 == "end":
                result = avg_list(items)
                print("Average is: ", result)
                quit()
            else:
                try:
                    items.append(num1)
                except:
                    print("Error: Bad input")
                    break

if __name__ == "__main__":
    prompt = avg()