def count_chars(str):
    result = {}

    for char in str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


print(count_chars("smiles"))
