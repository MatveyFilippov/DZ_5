print("Здесь можно первести число из десятичной системы счисления в двоичную или восьмеричную!")
print()
input("Чтобы продолжить нажмите ENTER")
NMB = int(input("Введите число: "))
print()
print("Выберите  2  если, чтоб число переволось в двоичную СС" )
print("Выберите  8  если хотите, чтоб число перевелось в восьмиричную СС" )
CHOICE = input("Введите 2 или 8: ")
def division(N, C, ONE):
    NNMB = ""
    while N != ONE:
        N = N // int(C)
        RMN = N % int(C)
        NNMB = str(NNMB) + str(RMN)
    RMN = N % int(C)
    NNMB = str(RMN) + str(NNMB)
    N = NNMB
    return N
while CHOICE != "2" and CHOICE != "8":
    CHOICE = input("Ошибка! Введите 2 или 8: ")
if CHOICE == "2":
    NMB = division(NMB, CHOICE, 1)
else:
    NMB = division(NMB, CHOICE, 7)
INV = ""
for i in range(len(NMB)):
    INV = NMB[i]+INV
NMB = INV
print(NMB)