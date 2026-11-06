def area_circle(radius):
    return 3.14159 * radius ** 2
def area_rectangle(a, b):
    return a * b
def area_triangle(base, height):
    return (base * height) / 2
def main():
    print("Оберіть фігуру:")
    print("1 — Коло")
    print("2 — Прямокутник")
    print("3 — Трикутник")
    choice = input("Ваш вибір: ")
    if choice == "1":
        radius = float(input("Введіть радіус: "))
        print("Площа круга:", area_circle(radius))
    elif choice == "2":
        a = float(input("Введіть ширину: "))
        b = float(input("Введіть висоту: "))
        print("Площа прямокутника:", area_rectangle(a, b))
    elif choice == "3":
        base = float(input("Введіть основу: "))
        height = float(input("Введіть висоту: "))
        print("Площа трикутника:", area_triangle(base, height))
    else:
        print("Невідомий вибір")
main()
