from wordl_solver.dataset import load_dataset
from wordl_solver.solver import solve_greedy


def main():
    guess = 1
    n = 5
    blacklist = list()
    forcelist = list()
    invalidposlist = list()
    print('wordl_solver by iMilchshake (https://github.com/iMilchshake/wordl_solver)')
    words = load_dataset()
    print("wordlist has been parsed\n")

    while True:
        word_canidates = solve_greedy(words, blacklist, forcelist, invalidposlist, n)
        if len(word_canidates) <= 0:
            raise Exception("no valid words found")
        display_canidates(word_canidates, guess)
        guess += 1
        if guess > 6:
            exit()

        try:
            blacklist += input('ban characters: ').replace(' ', '').split(',')
        except Exception as _:
            pass

        try:
            forcelist += list(map(lambda entry:
                                  (entry.split(' ')[0], int(entry.split(' ')[1])),
                                  input('force list: ').split(',')))
        except Exception as _:
            pass

        try:
            invalidposlist += list(map(lambda entry:
                                       (entry.split(' ')[0], [int(entry.split(' ')[1])]),
                                       input('invalid pos list: ').split(',')))
        except Exception as _:
            pass
        print("")


def display_canidates(word_canidates: iter, guess_number):
    print(('=' * 20) + f'[ GUESS {guess_number} ]' + ('=' * 20))
    for i, word in enumerate(word_canidates):
        print(f'{i}) - \'{word}\'')
    print(('=' * 51) + '\n')
