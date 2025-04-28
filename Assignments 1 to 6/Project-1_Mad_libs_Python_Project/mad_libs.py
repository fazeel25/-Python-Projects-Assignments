# Mad lib Game

def mad_libs():

    print("Welcome to Mad Libs! Fill in the blanks.")    
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    
    story = f"Once upon a time, in a {adjective} land called {place}, there was a {noun} who loved to {verb} all day long."
    print("\nHere is your Mad Libs story:")
    print(story)
    
if __name__ == "__main__":
    mad_libs()
