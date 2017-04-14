def progress_updater(guess, word, progress):
    i = 0
    while i < len(word):
        if guess == word[i]:
            progress[i] = guess
            i += 1
        else:
            i += 1

    return "".join(progress)


class Hangman():
    def __init__(self):
        print("Are you ready to die?")
        print("(a)Yeah, I'm here to die.\n(2)Scared!! Leave game.")
        user_choice_1 = input("->")

        if user_choice_1 == '1':
            print("Loading.....")
            self.start_game()
        elif user_choice_1 == '2':
            print("See ya!")
            exit()
        else:
            print("I'm sorry, can you repeat that?")
            self.__init__()

    def start_game(self):
        print("Countdown begins here.....Be ready to die!!")
        self.core_game()

    def core_game(self):
        guesses = 0
        LettersUsed = ""
        word = "python"
        progress = ["?", "?", "?", "?", "?"]

        while guesses < 6:
            guess = input("Guess a letter ->")

            if guess in word and not guess in LettersUsed:
                print("As it turns out, your guess was RIGHT!")
                LettersUsed += "," + guess
                self.hangman_graphic(guesses)
                print("Progress: " + progress_updater(guess, word, progress))
                print("Letter used: " + LettersUsed)
            elif guess not in word and not guess in LettersUsed:
                guesses += 1
                print("Sorry man! That guess was WRONG!")
                LettersUsed += "," + guess
                self.hangman_graphic(guesses)
                print("Progress: " + "".join(progress))
                print("Letter used: " + LettersUsed)
            else:
                print("That's the wrong letter, you wanna be out here all day?")
                print("Try again!")

    def hangman_graphic(self, guesses):
        if guesses == 0:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif guesses == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif guesses == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif guesses == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif guesses == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif guesses == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            print("The noose tightens around your neck, and you.....")
            print("GAME OVER!")
            self.__init__()


game = Hangman()