print("Здесь можно первести число из десятичной системы счисления в двоичную или восьмеричную!")
input("Чтобы продолжить нажмите ENTER")
print()
NMB = int(input("Введите число: "))
print("Выберите  2  если, чтоб число переволось в двоичную СС" )
print("Выберите  8  если хотите, чтоб число перевелось в восьмиричную СС" )
CHOICE = input("Введите 2 или 8: ")
def division(N, C, O):
    NNMB = ""
    while N > O:
        RMN = N % int(C)
        N = N // int(C)
        NNMB = str(NNMB) + str(RMN)
    RMN = N % int(C)
    NNMB = str(NNMB) + str(RMN)
    N = NNMB
    return N
while CHOICE != "2" and CHOICE != "8":
    CHOICE = input("Ошибка! Введите 2 или 8: ")
NMB = division(NMB, CHOICE, int(CHOICE) - 1)
INV = ""
for i in range(len(NMB)):
    INV = NMB[i] + INV
NMB = INV
print()
if CHOICE == "2":
    CHOICE = "двоичной"
else:
    CHOICE = "восмиричной"
print("Ваше число в", CHOICE, "системе счисления:", NMB)
print()
input("Чтобы завершить нажмите ENTER")