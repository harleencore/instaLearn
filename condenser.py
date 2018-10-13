import wikipedia
from sys import argv

while True:
    topic = input("\nEnter topic to be summarized: ")
    try:
        article = wikipedia.summary(topic)
        print("\n" + article)
    except Exception as e: print(e)
