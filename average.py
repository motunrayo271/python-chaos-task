total = 0.0
count = 0

while True:
    num = float(input("Enter a number (-1 to stop): "))
    
    if num == -1:
        break
        
    total += num
    count += 1
    average = total / count
    print(f"Current average: {average}")

