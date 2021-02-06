# Cube program

def cube_it(num1, num2, num3):
    try:
        if num1 > 0 and num2 > 0 and num3 > 0:
            value = num1 * num2 * num3
            return value
        else:
            print("Error: Negative number or zero passed")
            return
    except:
        print("Error: Bad input")
        return

class cube:
    def __init__(self):
        result = 0
        try:
            num1 = float(input("Calculate the volume of a cube!\nEnter first value: "))
            num2 = float(input("Enter second value: "))
            num3 = float(input("Enter third value: "))
            result = cube_it(num1, num2, num3)
            print(result)
        except:
            print("Bad input!")

if __name__ == "__main__":
    prompt = cube()