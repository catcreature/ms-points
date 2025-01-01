import time
import pyautogui as pyt

number_of_searches = int(input("Enter how many searches you want to perform."))

for i in range(number_of_searches):
    print(f"searching for the {i+1}")
    time.sleep(1)
    pyt.press("win")
    time.sleep(1)
    pyt.write(f"what is the power of 351 to {i}?")
    time.sleep(1)
    pyt.press("enter")
    time.sleep(10)