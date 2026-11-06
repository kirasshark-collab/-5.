
def minimum(grades):
    return min(grades)
def maximum(grades):
    return max(grades)
def count_above(grades, value):
    count = 0
    for grade in grades:
        if grade > value:
            count += 1
    return count
def main():
    grades = [10, 8, 12, 9, 11]
    value = 9
    print("Середній бал:", average(grades))
    print("Мінімальна оцінка:", minimum(grades))
    print("Максимальна оцінка:", maximum(grades))
    print("Оцінок вище", value, ":", count_above(grades, value))
main()
