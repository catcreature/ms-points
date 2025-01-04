import pyautogui as pyt
import wikipedia as wiki

number_of_searches = int(input("Enter how many searches you want to perform."))

def from_wiki():
    topic = wiki.random()
    print(topic)
    sentences = wiki.summary(topic,sentences=10).split(".")
    return sentences

sentence = from_wiki()
for i in range(number_of_searches):
    print(f"searching for the {i+1}")
    pyt.sleep(1)
    pyt.press("win")
    pyt.sleep(1)
    pyt.typewrite(sentence[i],0.1)
    pyt.sleep(1)
    pyt.press("enter")
    pyt.sleep(5)