def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    # Якщо upper_bound все ще None, це означає, що всі елементи менші за target
    return (iterations, upper_bound)

# Перевірка функції на прикладах
if __name__ == "__main__":
    # Відсортований масив з дробовими числами
    sorted_array = [1.1, 2.3, 3.5, 4.8, 5.9, 7.2, 8.6, 9.9]

    # Значення для пошуку
    test_values = [4.8, 6.0, 10.0, 0.5]

    # Перевірка пошуку для кожного значення
    for value in test_values:
        iterations, upper_bound = binary_search(sorted_array, value)
        print(f"Шукали: {value}, Ітерацій: {iterations}, Верхня межа: {upper_bound}")
