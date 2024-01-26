       
import pickle

def is_registered(username):
    with open("userdata.dat", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data["username"] == username.strip().lower():
                    return True
            except EOFError:
                file.close()
                break



def register(username , password ):
    
    data = {"username" : username.strip().lower() , "password":password.strip()}
    
    with open("userdata.dat" , "ab") as file:
            pickle.dump(data , file)
    
    
def user_good(username , password ):
    with open("userdata.dat", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data["username"] == username.strip().lower():
                    if data["password"]==password:
                        return True
            except EOFError:
                file.close()
                break