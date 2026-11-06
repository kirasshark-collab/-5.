def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result
def digit_sum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total
def main():
    number = int(input("Введіть натуральне число: "))
    if is_prime(number):
        print("Просте число: так")
    else:
        print("Просте число: ні")
    print("Дільники:", divisors(number))
    print("Сума цифр:", digit_sum(number))
main()
