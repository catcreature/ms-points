import time

number_of_searches = int(input("Enter how many searches you want to perform."))

for i in range(number_of_searches):
    print(f"searching for the {i+1}")
    time.sleep(1)