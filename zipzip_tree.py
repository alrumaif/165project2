from __future__ import annotations

from typing import TypeVar
from dataclasses import dataclass
import math
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

@dataclass
class Rank:
    geometric_rank: int
    uniform_rank: int

@dataclass
class Node:
    key: KeyType
    val: ValType
    rank: Rank
    left: KeyType = None
    right: KeyType = None

class ZipZipTree:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.height = 0
        self.tree = {}
        self.root = None

    def get_random_rank(self) -> Rank:
        geometric_rank = 0
        while random.getrandbits(1):
            geometric_rank += 1
        max_uniform = int(math.log(self.capacity) ** 3) if self.capacity > 1 else 0
        uniform_rank = random.randint(0, max(0, max_uniform - 1))
        return Rank(geometric_rank, uniform_rank)

    def insert(self, key: KeyType, val: ValType, rank: Rank = None):
        if rank is None:
            rank = self.get_random_rank()
        new_node = Node(key, val, rank)
        self.tree[key] = new_node

        cur, parent = self.root, None
        while cur is not None:
            cur_node = self.tree[cur]
            if (cur_node.rank.geometric_rank > rank.geometric_rank or
                (cur_node.rank.geometric_rank == rank.geometric_rank and
                 cur_node.rank.uniform_rank > rank.uniform_rank)):
                parent = cur
                cur = cur_node.left if key < cur_node.key else cur_node.right
            else:
                break

        if cur is not None:
            if key < self.tree[cur].key:
                new_node.right = cur
            else:
                new_node.left = cur

        if parent is None:
            self.root = key
        else:
            parent_node = self.tree[parent]
            if key < parent_node.key:
                parent_node.left = key
            else:
                parent_node.right = key

        self.size += 1

    def remove(self, key: KeyType):
        if key not in self.tree:
            return

        cur, prev = self.root, None
        while cur != key:
            prev = cur
            cur = self.tree[cur].left if key < self.tree[cur].key else self.tree[cur].right

        node = self.tree[cur]
        left, right = node.left, node.right

        if left is None or right is None:
            replacement = right if left is None else left
        else:
            left_rank = self.tree[left].rank.geometric_rank
            right_rank = self.tree[right].rank.geometric_rank
            replacement = left if left_rank <= right_rank else right

        if cur == self.root:
            self.root = replacement
        elif key < self.tree[prev].key:
            self.tree[prev].left = replacement
        else:
            self.tree[prev].right = replacement

        while left is not None and right is not None:
            if self.tree[left].rank.geometric_rank <= self.tree[right].rank.geometric_rank:
                while (left is not None and
                       self.tree[left].rank.geometric_rank <= self.tree[right].rank.geometric_rank):
                    prev = left
                    left = self.tree[left].right
                self.tree[prev].right = right
            else:
                while (right is not None and
                       self.tree[right].rank.geometric_rank < self.tree[left].rank.geometric_rank):
                    prev = right
                    right = self.tree[right].left
                self.tree[prev].left = left

        del self.tree[key]
        self.size -= 1

    def find(self, key: KeyType) -> ValType:
        cur = self.root
        while cur is not None:
            node = self.tree[cur]
            if key == node.key:
                return node.val
            cur = node.left if key < node.key else node.right
        raise KeyError(f"Key {key} not found")

    def get_size(self) -> int:
        return self.size

    def get_height(self) -> int:
        def height_recursive(node_key):
            if node_key is None:
                return -1
            node = self.tree[node_key]
            return 1 + max(height_recursive(node.left), height_recursive(node.right))
        return height_recursive(self.root)

    def get_depth(self, key: KeyType):
        cur, depth = self.root, 0
        while cur is not None:
            node = self.tree[cur]
            if key == node.key:
                return depth
            cur = node.left if key < node.key else node.right
            depth += 1
        raise KeyError(f"Key {key} not found")

