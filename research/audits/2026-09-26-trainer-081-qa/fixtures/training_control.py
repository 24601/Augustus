"""Alternative CPU training paths used by a local decision component."""
import torch
from torch import nn
from torch.nn import functional as F


class DecisionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Linear(2, 2)
        self.head = nn.Linear(2, 1)

    def forward(self, x):
        return self.head(torch.tanh(self.encoder(x))).squeeze(-1)


def make_optimizer(model, tune_encoder, lr):
    model.encoder.requires_grad_(tune_encoder)
    return torch.optim.SGD((p for p in model.parameters() if p.requires_grad), lr=lr)


def soft_loss(logits, target_mass):
    return F.binary_cross_entropy_with_logits(logits, target_mass)
