def separate_odd_even_num(filename):
    try:
        with open(filename, 'r') as num_file:
            # Read the first 20 integers from the file
            numbers = []
            for i in range(20):
                line = next(num_file, None)
                if line is None:
                    break
                num = int(line.strip())
                numbers.append(num)

            # Open the even.txt and odd.txt file
            with open('even.txt', 'w') as even_file:
                # Write the even numbers to the file
                for num in numbers:
                    if num % 2 == 0:
                        even_file.write(f'{num}\n')

        
            with open('odd.txt', 'w') as odd_file:
                # Write the odd numbers to the file
                for num in numbers:
                    if num % 2 != 0:
                        odd_file.write(f'{num}\n')

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

separate_odd_even_num('numbers.txt')