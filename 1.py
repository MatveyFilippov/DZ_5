print("Здесь можно первести число из десятичной системы счисления в двоичную или восьмеричную!")
print()
input("Чтобы продолжить нажмите ENTER")
NMB = float(input("Введите число: "))
print()
print("Выберите  2  если, чтоб число переволось в двоичную СС" )
print("Выберите  8  если хотите, чтоб число перевелось в восьмиричную СС" )
CHOICE = input("Введите 2 или 8: ")
NNMB = ""
def division(N, C, X):
    while N > X:
        N = N // C
        RMN = N % C
        NNMB = str(NNMB) + str(RMN)
    N = NNMB
    return N
while CHOICE != "2" and CHOICE != "8":
    CHOICE = input("Ошибка! Введите 2 или 8: ")
else:
    division(NMB, CHOICE, 1)
print(NMB)