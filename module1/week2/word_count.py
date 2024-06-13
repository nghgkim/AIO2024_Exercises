import os
cur = os.path.abspath(__file__)
file_path = os.path.dirname(cur).replace("\\", "/") + '/P1_data.txt'


def word_count(file_path):
    result = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            words = [word.lower() for word in words]
            for word in words:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
    return result


print(word_count(file_path))
