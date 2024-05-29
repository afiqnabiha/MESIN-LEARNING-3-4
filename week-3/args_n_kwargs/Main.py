'''
    program menghitung operasi matematika menggunakan *args dan **kwargs
    
    konsep:
    *args -> tuple
    **kwargs -> dictionary
    type hints = memberikan datatype pada argumen fungsi
    urutan operasi matematika {(*|/) (->) (+|-)}
    tanda kurung () diabaikan
    
'''

def tambah(x, y):
    if not (type(x) == int) or not (type(y) == int):
        raise Exception(f"unexpected type x, y: {type(x)}, {type(y)} \t expected type: <int>")
    return x + y

def kurang(x, y):
    if not (type(x) == int) or not (type(y) == int):
        raise Exception(f"unexpected type x, y: {type(x)}, {type(y)} \t expected type: <int>")
    return x - y

def kali(x, y):
    if not (type(x) == int) or not (type(y) == int):
        raise Exception(f"unexpected type x, y: {type(x)}, {type(y)} \t expected type: <int>")
    return x * y

def bagi(x, y):
    if not (type(x) == int) or not (type(y) == int):
        raise Exception(f"unexpected type x, y: {type(x)}, {type(y)} \t expected type: <int>")
    
    if y == 0:
        raise Exception("divide by 0")
    return x/y

def sortOperator(operator:list):
    # ["*", "x", "/", ":", "+", "-"]
    operators = [] 
    x = 0
    if not any(operator in ["*", "x", "/", ":", "+", "-"] for operator in ["*", "x", "/", ":", "+", "-"]):
        raise Exception(f"invalid operator type {operator}")
    for i in operator:
        if i in ["*", "x", "/", ":"]:
            operators.append(i)
    
    for i in operator:
        if i in ["+", "-"]:
            operators.append(i)
    
    return operators

def to_operator(list:str):
    return [x for x in list if x in ["+", "-", "*", "x", ":", "/"]]

def to_numberList(list:str):
    return [int(x) for x in list if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

def parse_input(input:str):
    # clear input string from text character
    input = str(filter(lambda x: x in ["+", "-", "*", "x", ":", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]))
    operator = to_operator(input)
    nums = to_numberList(input)
    
    return nums, operator
    
def negative(x):
    if not type(x) == int or type(x) == float:
        raise Exception("not number type")
    
    return x * (-1)

'''
contoh 1:
1 + 2 * 3 * 4 / 5 - 6
= (1 + 2 * 3 * 4 / 5) - 6
= (1 + (2 * 3) * (4 / 5)) - 6
= (1 + ((2 * 3) * (4 / 5)) ) - 6
= (1 + ((6) * (4/5))) - 6
= (1 + 24/5) - 6

contoh 2:
1 + 3 * 4 + 4 - 5 * 7 - 5 + 4 / 2
{*, *, /, +, +, -, -, +}
= 1 * 3 * 4 xxx ... salah

contoh 3:
1 + 3 * 4 + 4 - 5 * 7 - 5 + 4 / 2
{*, *, /, +, +, -, -, +}
= 3 * 4 * ... salah juga

contoh 4:
1 + 3 * 4 + 4 - 5 * 7 - 5 + 4 / 2
a = 3 * 4
b = 5 * 7
c = 4 / 2
d = 1 + a -> 1 + 3 * 4
e = d + 4 -> 1 + 3 * 4 + 4
f = e - b -> 1 + 3 * 4 + 4 - 5 * 7
g = f - 5 + c -> (((1 + (3 * 4)) + 4) - (5 * 7)) - 5 + (4/2)
1 + 3 * 4 + 4 - 5 * 7 - 5 + 4 / 2 = g


{1, 3, 4, 4, 5, 7, 5, 4, 2}
{'+', '*', '+', '-', '*', '-', '+', '/'}



cari operator kali atau bagi, lakukan operasi dgn operand angka i dan angka i+1
cari operator + dan -, lakukan operasi yang sama
1 + 3 * 4 + 4 - 5 * 7 - 5 + 4 / 2
1 + (3 * 4) + 4 - (5 * 7) - 5 + (4 / 2)

'''

def hitung(angka:list, operator:list):
    if len(operator) != len(angka) - 1:
        raise Exception("overflow of length operator")
    # len_of_num = len(angka)
    # len_of_ops = len(operator)
    if -1 in angka:
        raise Exception("cannot receive -1 value")
    
    hasil = []
    indeks = []
    # ops = sortOperator(operator.copy())
    # kali dan bagi
    i = 0
    while i < len(operator):
        if operator[i] == "*" or operator[i] == "x":
            hasil.append(kali(angka[i], angka[i+1]))
            indeks.append(i)
            indeks.append(i+1)
            
        elif operator[i] == "/" or operator[i] == ":":
            hasil.append(bagi(angka[i], angka[i+1]))
            indeks.append(i)
            indeks.append(i+1)
            
        i+=1
    
    # mengubah angka redundan menjadi -1: {operand untuk perkalian dan pembagian} 
    i = 0
    while i < len(angka):
        if i in indeks:
            angka[i] = 0.1
        i+=1
    # print(f"angka <before>:\t {angka}")
    
    # menghapus indeks yang tidak dibutuhkan
    i = 0
    while i < round(len(indeks)/2):
        indeks.pop(i+1)
        i+=1
    # print(f"indeks: {indeks}\n")

    # mengganti -1 menjadi hasil
    i = 0
    for x in indeks:
        angka[x] = hasil[i]
        i+=1
    
    
    # menghapus angka bertipe float
    angka = list(filter(lambda x: type(x) == int, angka))
    # print(f"final:\t {angka}")
    
    # memfilter operator agar tidak ada operator * dan /
    operator = list(filter(lambda o: not o in ["*", "x", "/", ":"], operator))
    
    # mencari operator -
    i = 0
    for x in operator:
        if len(operator) != len(angka) - 1:
            print("cannot proccess negative operator ... proccess terminated\n")
            break
        elif x == "-":
            # mengkonversi item menjadi negatif
            angka[i+1] = negative(angka[i+1])
        i+=1
    
    return sum(angka)
            
    
    


print(f"hasil: {hitung([1, 2, 3, 4, 5, 6, 2], operator=['+', '*', '+', '-', '*', '-'])}")
'''

[1, 2, 3, 4, 5, 6]
1 + 2 * 3 + 4 - 5 * 6 - 2
= {(2 * 3), (5*6)} .... {2, 3, 5, 6} .. {1, 2, 4, 5}
= {->1, (2 * 3), ->4, (5*6), 2}

'''