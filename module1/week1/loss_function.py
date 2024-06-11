import random
import math


def loss_function(num_samples, loss_name):
    result = ""

    predict = -1
    target = -1
    loss = 0

    if loss_name == 'MAE':
        for i in range(num_samples):
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            loss = loss + abs(target - predict)

            result = result + f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {abs(target - predict)}\n'

        result = result + f'final MSE: {loss / num_samples}'
    elif loss_name == ' MSE':
        for i in range(num_samples):
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            loss = loss + (target - predict) ** 2

            result = result + f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {(target - predict) ** 2}\n'

        result = result + f'final MSE: {loss / num_samples}'
    elif loss_name == 'RMSE':
        for i in range(num_samples):
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            loss = loss + (target - predict) ** 2

            result = result + f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {(target - predict) ** 2}\n'

        result = result + f'final RMSE: {math.sqrt(loss / num_samples)}'
        
    return result


def exercise3():
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        return 'number of samples must be an integer number'
    
    loss_name = input('Input loss name: ')
    return loss_function(int(num_samples), loss_name)

print(exercise3())