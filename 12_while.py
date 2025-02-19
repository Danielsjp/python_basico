"""
WHILE = mientras
"""

num = 5
# while num > 0:
#     print(num)
#     num -= 1
# else:
#     print("has entrado en el else")

# print ("#"*20)
# while True:
#     print(num)
#     num -= 1
#     if num == 0:
#         print("has llegado al final")
#         break

monedas = 10

while True:
    dinero = int(input("Cuanto dinero necesitas?"))
    monedas = monedas - dinero
    print(f"me quedan {monedas}")
    if monedas < 1:
        print("no queda dinero")
        break

    