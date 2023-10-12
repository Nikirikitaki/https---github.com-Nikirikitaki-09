import sys
phone_book = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            print("No enough parameter,try again ")
            
        except ValueError:
            print("No correct parametr,try again ")
        except KeyError:
            print("No correct name")
    return inner
            

def greeting():
    print ("How can I help you?")
    


def add_new_phone(name,phone):
    
    phone_book.update({name: phone})
    print("phone added")
    

def change_phone(name,phone):
    
    phone_book[name] = phone
    print("phone changed") 
    
    

def phone_info(name):
    print (phone_book.get(name))
    


def show_all():
    for key, value in phone_book.items():
        print(f"Name: {key}, Number : {value}")
    

def good_bye():
    print("good bye")
    sys.exit()
    
@input_error
def parser(name:str):
    name_lower = name.lower()
    if name_lower.endswith('.') :
        good_bye()
    if name_lower == "hello":
        greeting()
    
    if name_lower.startswith("add"):
        split_words = name_lower.split()
        name = split_words[1]
        phone = int(split_words[2])
        add_new_phone(name,phone)
    
    if name_lower.startswith("change"):
        split_words = name_lower.split()
        name = split_words[1]
        phone = int(split_words[2])
        change_phone(name,phone)
    
    if name_lower.startswith("phone"):
        split_words = name_lower.split()
        name = split_words[1]
        phone_info(name)
    
    if name_lower == "show all":
        show_all()
    
    if  name_lower in ["good bye", "close", "exit"]:
        good_bye()
    
def main() :
    while True:
        user_input = parser(input("Write you command here: "))
        

if __name__ == '__main__':
    main()


    