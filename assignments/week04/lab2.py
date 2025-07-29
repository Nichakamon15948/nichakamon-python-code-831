"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average #โชว์3ตัวนี้


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        numbers.append(int(input("Enter number [" + str(i) + "]: ")))

    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers =[] # Your code here
    odd_numbers =[] # Your code here
    
    # Calculate average
    average = sum(numbers) / len(numbers) # Your code here
    
    # Numbers greater than average
    above_average = [] # Your code here
    
    for i in range(10):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])

        if numbers[i] > average:
            above_average.append(numbers[i])

    # Display results
    # Your code here
    print("Even Number: ", even_numbers)
    print("Odd Number:" , odd_numbers)
    print("Above Average: ", above_average)
    print("Sum: ", sum(numbers))
    print("Average:", average)
    print("Min: ", min(numbers))
    print("Max: ", max(numbers))

if __name__ == "__main__":
    number_operations()

