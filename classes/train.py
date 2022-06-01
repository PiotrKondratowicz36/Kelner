import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision
from torch.utils.data import DataLoader
from customDataset import PlatesDataset

# Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Parameters
learning_rate = 1e-3  # wykorzystywany przy w decyzji w jakim kierunku należy zmienić wagi żeby błąd popełniany przez sieć zmalał
batch_size = 16  # odpowiada za ilosc przykladow branych do kazdego treningu
num_epochs = 1  # okresla, ile razy algorytm widzi caly zbior danych
# mean = [0.7676, 0.7290, 0.6800], std = [0.1982, 0.2108, 0.2328]


# Load Data
dataset = PlatesDataset(csv_file='fullandemptyplates.csv', root_dir='allplatesresized',
                        transform=transforms.ToTensor())

train_set, test_set = torch.utils.data.random_split(dataset, [1650, 350])
train_loader = DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_set, batch_size=batch_size, shuffle=True)

# Model
model = torchvision.models.googlenet(pretrained=True) # 22 layers
model.to(device)

# Loss and optimizer to reduce losses
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


# Train Network
for epoch in range(num_epochs):
    losses = []

    for batch_idx, (data,targets) in enumerate(train_loader):
        # Get data to cuda if possible
        data = data.to(device=device)
        targets = targets.to(device=device)

        # forward
        scores = model(data)
        loss = criterion(scores, targets)

        losses.append(loss.item())

        # backward
        optimizer.zero_grad()
        loss.backward()

        # gradient descent or adam step
        optimizer.step()

   # print(f'Cost at epoch {epoch} is {sum(losses)/len(losses)}')

torch.save(model, 'recognizeplate.pth')


def check_accuracy(loader, model):
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device=device)
            y = y.to(device=device)

            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)

        print(f'Got {num_correct} / {num_samples} with accuracy {float(num_correct)/float(num_samples)*100}%')

    model.train()

print("Checking accuracy on Training Set")
check_accuracy(train_loader, model)

print("Checking accuracy on Test Set")
check_accuracy(test_loader, model)