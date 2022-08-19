def cekParitas(bilangan):
    if int(bilangan) % 2 == 0:
        print(bilangan, "adalah bilangan genap")
    else:
        print(bilangan, "adalah bilangan ganjil")

if __name__ == "__main__":
    bilangan = input('Masukan bilangan: ')
    cekParitas(bilangan)
