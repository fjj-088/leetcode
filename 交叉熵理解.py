import torch
import torch.nn.functional as F

# 假设我们有两个批次，每个批次有三个类别的logits
logits = torch.tensor([[1.2, 0.9, 0.3],
                      [2.1, 1.4, -0.4]])

# 应用softmax函数，指定dim=0，即沿着第一个维度（批次维度）进行softmax
probabilities = F.softmax(logits, dim=0)

print(probabilities)
print(F.softmax(torch.tensor([1.2, 2.1]), dim=0))