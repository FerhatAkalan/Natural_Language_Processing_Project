import torch
from torch.utils.data import DataLoader

from ChunkingDataset import ChunkingDataset
from ChunkingLoader import ChunkingLoader
from LSTMClassifier import LSTMClassifier

vocab_size = 20000
embed_dim = 32
hidden_dim = 64
num_classes = 3
batch_size = 32
epochs = 5
lr = 0.001

# Dataset and DataLoader
chunking_loader = ChunkingLoader("resources/")
dataset = ChunkingDataset(chunking_loader)
loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Model, Loss, Optimizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = LSTMClassifier(vocab_size, embed_dim, hidden_dim, num_classes).to(device)
criterion = torch.nn.BCELoss
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

# Training
for epoch in range(epochs):
    total_loss = 0
    for batch_x, batch_y in loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)

        optimizer.zero_grad()
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch + 1}/{epochs}, Loss: {total_loss:.4f}")