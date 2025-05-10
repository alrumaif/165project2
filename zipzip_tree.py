# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

from __future__ import annotations

from typing import TypeVar
from dataclasses import dataclass

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
		import math
		import random
		geometric_rank = 0
		while random.getrandbits(1):
			geometric_rank += 1
		if self.capacity <= 1:
			uniform_rank = 0
		else:
			max_uniform = int(math.log(self.capacity) ** 3)
			uniform_rank = random.randint(0, max(0, max_uniform - 1))
		return Rank(geometric_rank, uniform_rank)
	
	def insert(self, key: KeyType, val: ValType, rank: Rank = None):
		if rank is None:
			rank = self.get_random_rank()
		new_node = Node(key, val, rank)
		self.tree[key] = new_node
		cur = self.root
		parent = None
		while cur is not None:
			cur_node = self.tree[cur]
			if (cur_node.rank.geometric_rank < rank.geometric_rank or
                (cur_node.rank.geometric_rank == rank.geometric_rank and
                cur_node.rank.uniform_rank < rank.uniform_rank)):
				parent = cur
				if key < cur_node.key:
					cur = cur_node.left
				else:
					cur = cur_node.right
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
		cur = self.root
		parent = None
		while cur != key:
			parent = cur
			if key < self.tree[cur].key:
				cur = self.tree[cur].left
			else:
				cur = self.tree[cur].right
		node = self.tree[cur]
		left = node.left
		right = node.right
		if left is None:
			replacement = right
		elif right is None:
			replacement = left
		elif self.tree[left].rank.geometric_rank <= self.tree[right].rank.geometric_rank:
			replacement = left
		else:
			replacement = right
		if cur == self.root:
			self.root = replacement
		elif key < self.tree[parent].key:
			self.tree[parent].left = replacement
		else:
			self.tree[parent].right = replacement
		while left is not None and right is not None:
			if self.tree[left].rank.geometric_rank <= self.tree[right].rank.geometric_rank:
				while left is not None and self.tree[left].rank.geometric_rank <= self.tree[right].rank.geometric_rank:
					parent = left
					left = self.tree[left].right
				self.tree[parent].right = right
			else:
				while right is not None and self.tree[right].rank.geometric_rank < self.tree[left].rank.geometric_rank:
					parent = right
					right = self.tree[right].left
				self.tree[parent].left = left
		del self.tree[key]
		self.size -= 1


	

	def find(self, key: KeyType) -> ValType:
		cur = self.root
		while cur is not None:
			node = self.tree[cur]
			if key == node.key:
				return node.val
			elif key < node.key:
				cur = node.left
			else:
				cur = node.right
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
		cur = self.root
		depth = 0
		while cur is not None:
			node = self.tree[cur]
			if key == node.key:
				return depth
			elif key < node.key:
				cur = node.left
			else:
				cur = node.right
			depth += 1
		raise KeyError(f"Key {key} not found")
    
    


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
