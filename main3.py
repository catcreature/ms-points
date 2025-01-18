import wikipedia
import pyautogui

total_points = int(input("Enter total number of points you can earn."))
points_earned = int(input("Enter total number of points you have earned."))

number_of_searches = abs((total_points-points_earned)/3)+1

sentences =[]

def sentence_from_wiki():
    topic = wikipedia.random()
    print(f"Topic searched is {topic}.")
    try:
        summary = wikipedia.summary(title=topic)
    except wikipedia.exceptions.DisambiguationError:
        return sentences
    new_sentences = summary.split(".")
    for sentence_1 in new_sentences:
        if len(sentence_1)>30:
            sentences.append(sentence_1)
    print(f"Total number of sentences gathered are {len(sentences)}.")

sentence_from_wiki()

while len(sentences)<number_of_searches:
    print("Adding few more sentences.")
    sentence_from_wiki()

for nums,sentence in enumerate(sentences):
    print(f"Searches remaining {len(sentences)-nums}.")
    pyautogui.press("win")
    pyautogui.sleep(1.5)
    pyautogui.typewrite(sentence,0.1)
    pyautogui.sleep(1.5)
    pyautogui.press("enter")