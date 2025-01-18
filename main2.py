import time
import wikipedia as wiki

total_points = int(input("Enter total number of points."))
points_earned = int(input("Enter the points you have earned."))

def number_of_searches():
    print(int((total_points - points_earned) / 3))
    return int((total_points-points_earned)/3)

def valid_sentence_maker(generated_sentences):
    valid_sentences = []
    if len(generated_sentences)<30:
        print("Total number of generated sentences are less than the required sentences to search.")
    else:
        print("Required number of sentences are made.")

number_of_searches()

def from_wiki():
    topic = wiki.random()
    print(topic)
    sentences = wiki.summary(topic,sentences=10).split(".")
    print(f"The total number of sentences formed are {len(sentences)}")
    return sentences

# def main():
#     if number_of_searches()==0:
#         print("You have earned the maximum points possible.")
#         return
#     sentence = from_wiki()
#     for i in range(number_of_searches()):
#         print(f"searching for the {i+1}")
#         print(sentence[i])
#         time.sleep(1)
# main()