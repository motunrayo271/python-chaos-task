for hundreds in range(1, 10):
    for tens in range(0, 10):
        for units in range(0, 10):
            number = (hundreds * 100) + (tens * 10) + units
            sum_of_squares = (hundreds ** 2) + (tens ** 2) + (units ** 2)
            
            if sum_of_squares == number:
                print(number)

