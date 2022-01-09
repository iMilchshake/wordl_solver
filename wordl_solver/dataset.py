import csv


def load_dataset():
    path = 'data/wordsFreq.csv'

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)

        words5 = list()
        for i, row in enumerate(csv_reader):
            if len(row[1]) == 5:
                words5.append(row[1])

    return words5


if __name__ == '__main__':
    words = load_dataset()
    print('done', len(words))
    print(words[:10])
