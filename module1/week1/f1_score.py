def exercise1(tp: int, fp: int, fn: int):
    if type(tp) is not int:
        return "tp must be int"
    elif type(fp) is not int:
        return "fp must be int"
    elif type(fn) is not int:
        return "fn must be int"
    elif tp <= 0 or fp <= 0 or fn <= 0:
        return "tp and fp and fn must be greater than zero"
    else:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1_score = 2 * ((precision * recall) / (precision + recall))

        return f'precision is {precision}\nrecall is {recall}\nf1-score is {f1_score}'

print(exercise1(tp = 2, fp = 3, fn = 4))