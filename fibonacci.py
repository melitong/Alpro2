def CheckNumber(bilangan):
    isNumber = bilangan.isnumeric()
    return isNumber

def fibonacci(bilangan):
    n_1 = 0  
    n_2 = 1  
    count = 0
    if int(bilangan) <= 0:  
        print ("Please enter a positive integer, the given number is not valid")  
    # if there is only one term, it will return n_1  
    elif int(bilangan) == 1:  
        print ("The Fibonacci sequence of the numbers up to", int(bilangan), ": ")
        print(n_1) 
    else:  
        print ("The fibonacci sequence of the numbers is:")  
        while count < int(bilangan):  
            print(n_1)  
            nth = n_1 + n_2  
            # At last, we will update values  
            n_1 = n_2  
            n_2 = nth  
            count += 1 

if __name__ == "__main__":
    bilangan = input('Masukan bilangan: ')
    if(CheckNumber(bilangan)):
        fibonacci(bilangan)
    else:
        print("Masukkan Angka!")