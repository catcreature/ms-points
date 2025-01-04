import pyautogui as pyt
import wikipedia as wiki

total_points = int(input("Enter total number of points."))
points_earned = int(input("Enter the points you have earned."))

def number_of_searches():
    print(int((total_points - points_earned) / 3))
    return int((total_points-points_earned)/3)

def from_wiki():
    topic = wiki.random()
    print(topic)
    sentences = wiki.summary(topic,sentences=10).split(".")
    return sentences

def main():
    sentence = from_wiki()
    for i in range(number_of_searches()):
        print(f"searching for the {i+1}")
        pyt.sleep(1)
        pyt.press("win")
        pyt.sleep(1)
        pyt.typewrite(sentence[i],0.1)
        pyt.sleep(1)
        pyt.press("enter")
        pyt.sleep(4)
main()