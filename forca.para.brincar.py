import random
def draw_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    tries = min(len(stages) - 1, max(tries, 0))
    return stages[tries]
    

def pick_random_word():
    words = ["feliz-dia-das-mulheres", "Iona", "Ingrid", "rosa"]
    return random.choice(words)

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 20
    print("Vamos jogar Forca!")
    print(draw_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Por favor, adivinhe uma letra ou palavra: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Você já tentou ", guess)
            elif guess not in word:
                print(guess, "não está na palavra.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Boa!", guess, "está na palavra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Você já tentou a palavra ", guess)
            elif guess != word:
                print(guess, "não é a palavra.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Inválido.")
        print(draw_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Parabéns, você adivinhou a palavra! Você venceu!")
    else:
        print("Você perdeu!. A palavra era " + word + ".")

def main():
    word = pick_random_word()
    play(word)
    while input("Jogar de novo? (S/N) ").upper() == "S":
        word = pick_random_word()
        play(word)

if __name__ == "__main__":
    main()