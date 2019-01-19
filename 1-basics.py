import torch
import numpy as np

torch.manual_seed(42)

# declare dimension
input_size = 4
hidden_size = 2

# singleton example
# input_data_np = np.array([[[1, 0, 0, 0]]])

# sequential example
h = [1, 0, 0, 0]
e = [0, 1, 0, 0]
l = [0, 0, 1, 0]
o = [0, 0, 0, 1]
input_data_np = np.array([[h, e, l, l, o], [e, o, l, l, l], [l, l, e, e, l]], dtype=np.float32)

# transform as torch tensor
input_data = torch.Tensor(input_data_np).float()

# declare RNN
rnn = torch.nn.RNN(input_size, hidden_size)

# check output
outputs, _status = rnn(input_data)
print(outputs)
print(outputs.size())
