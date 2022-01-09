from wordl_solver.dataset import load_dataset


def solve_greedy(words: iter, char_blacklist: iter, char_forcelist: iter, char_invalidpos_list: iter, n=1):
    """ greedy solver that returns the first word in words that fulfills the conditions
        words: dataset from load_dataset()
        char_blacklist: list of banned characters
        char_forcelist: list of known character-positions
                        ('a', 2) will force an 'a' at index 2
        char_invalidpos_list: list of known characters (must occur at least once!), and their invalid positions
                              ('b', [0, 1, 2, 4]) will only allow 'b' at index 3
     """
    word_canidates = list()
    for word in words:
        if check_conditions(word, char_blacklist, char_forcelist, char_invalidpos_list):
            word_canidates.append(word)
            if len(word_canidates) >= n:
                break
    return word_canidates


def check_conditions(word, char_blacklist: iter, char_forcelist: iter, char_invalidpos_list: iter):
    # check blacklist
    if any(i in word for i in char_blacklist):
        return False

    # check forcelist
    for forced_char, forced_pos in char_forcelist:
        if word[forced_pos] != forced_char:
            return False

    # check known characters
    for known_char, _ in char_invalidpos_list:
        if known_char not in word:
            return False

    # check invalidpos
    for invalidpos_char, invalid_pos in char_invalidpos_list:
        for pos in invalid_pos:
            if word[pos] == invalidpos_char:
                return False

    return True


if __name__ == '__main__':
    dataset = load_dataset()
    res = solve_greedy(dataset, ['a', 'b', 'u', 't', 'w', 'l', 'd', 'f', 'c', 'h', 's', 'j'],
                       [('o', 1), ('r', 2), ('e', 4)],
                       [], n=5)
    print(f'try \'{res}\'')
