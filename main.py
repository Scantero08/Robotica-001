import math

radio = float(input("Radio del círculo: "))
perimetro = 2 * math.pi * radio
area = math.pi * radio ** 2
volumen = (4/3) * math.pi * radio **2
print(f"Volumen: {volumen:.2f}")
print(f"\nCírculo de radio {radio}:")
print(f"Perímetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")

# Ejecutar el script
# $ python main.py
# Radio del círculo: 10
