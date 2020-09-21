#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List

def convert_to_absolute() -> float:
    return abs(float(input("Enter a number : ")))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    noms = []
    for letter in prefixes:
        noms.append(letter + suffixes)
    return noms


def prime_integer_summation() -> int:
    primes = []
    n = 2
    while len(primes) != 100:
        i = 2
        while i < n and n % i != 0:
            i += 1

        if i == n:
            primes.append(n)
        n += 1
    return sum(primes)


def factorial(number: int) -> int:
    if number == 0:
        return 1
    elif number == 1:
        return 1

    product = 1
    for i in range(1, number):
        product *= i
    return product


def use_continue() -> None:
    for number in range(1, 11):
        if number == 5:
            continue
        else:
            print(number)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
