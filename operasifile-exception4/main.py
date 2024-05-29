import menu
print(4*"=", " selamat datang", 4*"=", "\n")

def konsol():
    print("pilih menu:")
    print("1. membaca file")
    print("2. menulis file")
    print("3. hapus file")
    print("4. exit")
    pilih = int(input())
    if pilih > 0 and pilih <= 4:
        print(f"melakukan menu {pilih}\n")
        match pilih:
            case 1:
                menu.readFile()
                konsol()
            case 2:
                menu.writefile()
                konsol()
            case 3:
                menu.removeFile()
                konsol()
            case _:
                return menu.exit()
    else:
        print(f"opsi {pilih} tidak tersedia")
        konsol()

konsol()