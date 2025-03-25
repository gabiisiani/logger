print("Hi :)")



start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

even_sum = sum(num for num in range(start, end + 1) if num % 2 == 0)

print(f"The sum of even numbers from {start} to {end} is {even_sum}")
