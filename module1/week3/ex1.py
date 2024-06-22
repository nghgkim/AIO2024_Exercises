import torch
import torch.nn as nn


class MySoftmax (nn . Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0)


class SoftmaxStable(nn.Module):
  def __init__(self):
    super().__init__()

  def forward(self, x):
    x_max = torch.max(x, dim = 0, keepdims = True)
    x_exp = torch.exp (x - x_max.values)
    partition = x_exp.sum (0 , keepdims = True)
    return x_exp / partition


data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
