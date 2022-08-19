def CheckNumber(bilangan):
    isNumber = bilangan.isnumeric()
    return isNumber

if __name__ == "__main__":
    bilangan = input('Masukan bilangan: ')
    if(CheckNumber(bilangan)):
        print("Anda memasukkan angka ", bilangan)
    else:
        print("Masukkan Angka!")