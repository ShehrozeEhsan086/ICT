codes = {'1':'[','2':'_','3':')','4':'}','5':']','6':'{'}
def encryptMessage(string):
    
    return codes[string]

def main():
    string = input("Enter (1-6): ")
    msg = encryptMessage(string)
    print(msg)
    
main()