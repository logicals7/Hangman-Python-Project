# Write your code here
import random

class Hangman:
    def __init__(self):
        print("H A N G M A N")
        #self.words = ['javascript']
        self.words = ['python', 'java', 'kotlin', 'javascript'] # list of words
        self.ran_ = random.choice(self.words)  # chooses the random word from the words
        self.x = list(len(self.ran_) * '-')
        self.count = 0  # counts the attempts remaining
        self.asked_letters = set()
        self.list_ran_ = []  # list of letters of randomly chosen word

        # Putting the letters of the randomly chosen word in a separate list
        # to identify it later that the asked letter is in this list or not.
        for letter in self.ran_:
            self.list_ran_.append(letter)

    # Giving result
    def result(self):
        # if list(letters of random words) == list(letters of scraped ____)
        if self.list_ran_ == self.x and self.count <= 8:
            print("You guessed the word {}!".format(self.ran_))
            print("You survived!\n")

        elif self.list_ran_ != self.x and self.count == 8:
            print("You lost!\n")

    # Replaces chars with ____
    def replace_char(self):
        # only runs when attempts are less than 8 & word is not guessed.
        while self.count != 8 and self.list_ran_ != self.x:
            print()
            print(*self.x, sep='')  # unpacks the list of guessed letters & prints it like -a-a--ript
            ask_letter = input("Input a letter: ")

            # if length of letter is more than 1
            if len(ask_letter) != 1:
                print("You should input a single letter")

            else:
                # if asked letter is in the random word chosen
                if ask_letter in self.ran_:
                    for index, element in enumerate(self.ran_):
                        if element == ask_letter:
                            self.x[index] = ask_letter

                    if ask_letter in self.asked_letters:
                        # self.count += 1
                        print("You already typed this letter")

                    self.asked_letters.add(ask_letter)

                else:
                    if ask_letter in self.asked_letters:
                        print("""You already typed this letter""")

                    elif ask_letter not in 'abcdefghijklmnopqrstuvwxyz':
                        print("It is not an ASCII lowercase letter")

                    else:
                        print("No such letter in the word")
                        self.count += 1
                        self.asked_letters.add(ask_letter)

    def play(self):
        while True:
            menu = input("""Type "play" to play the game, "exit" to quit: """)
            if menu == 'play':
                self.replace_char()
                self.result()

            elif menu == 'exit':
                exit()

# Driver Code
game = Hangman()
game.play()

