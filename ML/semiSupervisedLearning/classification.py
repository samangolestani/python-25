import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset
import numpy as np
import random

# Set seed for reproduciblity
seed = 42
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)

# Define transformations
transform=  transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),
 ])

# Load CIFAR-10 dataset
train_dataset = datasets.CIFAR10(root='./data', train=True,download=True, transform=transform)

test_dataset = datasets.CIFAR10(root='./data',train=False,transform=transform)

# Consider only a small fraction of labeled data
n_labeled = 5000
labeled_indices = np.random.choice(len(train_dataset), n_labeled,replace=False)
unlabeled_indices = np.array(list(set(range(len(train_dataset)))- set(labeled_indices)))

# Create subset

labeled_dataset = Subset(train_dataset, labeled_indices)
unlabeled_dataset = Subset(train_dataset, unlabeled_indices)

# Create data loaders

labeled_loader = DataLoader(labeled_dataset,batch_size=64, shuffle=True)
unlabeled_loader = DataLoader(unlabeled_dataset,batch_size=64,shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# Define a simple Convolutional Neural Network

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN,self).__init__()
        self.conv1 = nn. Conv2d(3,32,kernel_size=3,padding=1)
        self.conv2 = nn.Conv2d(32,64,kernel_size=3,padding=1)
        self.fc1 = nn.Linear(64*8*8,128)
        self.fc2 = nn.Linear(128,10)
    def forward(self,x):
        x = nn.ReLU()(self.conv1(x))
        x = nn.MaxPool2d(kernel_size=2,stride=2)(x)
        x= nn.ReLU()(self.conv2(x))
        x = nn.MaxPool2d(kernel_size=2, stride=2)(x)
        x= x.view(x.size(0), -1)
        x = nn.ReLU()(self.fc1(x))
        x = self.fc2(x)
        return x
    
# Initialize models, loss fnuction, and optimizer
model = SimpleCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training Loop
for epoch in range(10):
    model.train()
    # Training eith labeled data 
    for data, labels in labeled_loader:
        optimizer.zero_grad()
        outputs = model(data)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    print(f"Epoch [{epoch+1}/10]completed")

# Evaluate on Test Data
model.eval()
correct =0
total = 0

with torch.no_grad():
    for data, labels in test_loader:
        outputs = model(data)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy on test set : {100 * correct/total:.2f}%')
