# Cube program

def combine_names(first, last):
    try:
        full_name = first + " " + last
        return full_name
    except:
        print("Error: Invalid values")

class prompter:
    def __init__(self):
        first = input("Enter first name: ")
        last = input("Enter last name: ")
        full_name = combine_names(first, last)
        print(full_name)
        

if __name__ == "__main__":
    prompt = prompter()