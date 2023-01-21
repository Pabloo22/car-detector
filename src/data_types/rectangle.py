from typing import Tuple
from dataclasses import dataclass


@dataclass
class Rectangle:

    x: int
    y: int
    w: int
    h: int

    def __iter__(self):
        return iter((self.x, self.y, self.w, self.h))

    def __getitem__(self, key):
        return (self.x, self.y, self.w, self.h)[key]

    def __len__(self):
        return 4

    def __contains__(self, item: Tuple[int, int]):
        x, y = item
        return self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h
