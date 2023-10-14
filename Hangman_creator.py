import hangman_project


hangman = hangman_project.Hangman('C:\Users\Dell\Desktop\Python Projects\Hangman-Game\words.txt')
hangman.choose_the_word()
hangman.fill_the_word_status()
while True:
    hangman.get_word_status()
    hangman.guess_the_letter()

    if hangman.attempts_remaining == 0:
        print("Out of attempts. The word was {}. Game over!".format(hangman.chosen_word))
        break

    elif hangman.chosen_word == ''.join(hangman.word_status):
        print("Hurray! You won the game!")
        break