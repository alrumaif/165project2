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
		import random
		geometric_rank = random.randint(0, self.capacity - 1)
		uniform_rank = random.randint(0, self.capacity - 1)
		return Rank(geometric_rank, uniform_rank)	
	
	def insert(self, key: KeyType, val: ValType, rank: Rank = None):
		if rank is None:
			rank = self.get_random_rank()
		x = Node(key, val, rank)
		cur = self.root
		prev = None
		while cur is not None:
			cur_node = self.tree[cur]
			if (rank.geometric_rank < cur_node.rank.geometric_rank or (rank.geometric_rank == cur_node.rank.geometric_rank and rank.uniform_rank < cur_node.rank.uniform_rank)):
				break
			prev = cur
			if key < cur_node.key:
				cur = cur_node.left
			else:
				cur = cur_node.right
		if prev is None:
			self.root = key
		else:
			parent = self.tree[prev]
			if key < parent.key:
				parent.left = key
			else:
				parent.right = key
				
		if cur is None:
			x.left = x.right = None
		else:
			if key < self.tree[cur].key:
				x.right = cur
			else:
				x.left = cur
		self.tree[key] = x
		self.size += 1
		prev = key
		if cur is not None:
			prev_node = self.tree[prev]
			if self.tree[cur].key < key:
				while cur is not None and self.tree[cur].key < key:
					prev = cur
					cur = self.tree[cur].right
				self.tree[prev].right = cur
			else:
				while cur is not None and self.tree[cur].key > key:
					prev = cur
					cur = self.tree[cur].left
				self.tree[prev].left = cur


	def remove(self, key: KeyType):
		if key not in self.tree:
			return 
		x = self.tree[key]
		cur = self.root
		prev = None
		while cur != key:
			prev = cur
			if key < self.tree[cur].key:
				cur = self.tree[cur].left
			else:
				cur = self.tree[cur].right
		node = self.tree[cur]
		left = node.left
		right = node.right
		if left is None:
			cur = right
		elif right is None:
			cur = left
		elif self.tree[left].rank.geometric_rank >= self.tree[right].rank.geometric_rank:
			cur = left
		else:
			cur = right
			
		if self.root == key:
			self.root = cur
		elif key < self.tree[prev].key:
			self.tree[prev].left = cur
		else:
			self.tree[prev].right = cur
			
		while left is not None and right is not None:
			if self.tree[left].rank.geometric_rank >= self.tree[right].rank.geometric_rank:
				while left is not None and self.tree[left].rank.geometric_rank >= self.tree[right].rank.geometric_rank:
					prev = left
					left = self.tree[left].left
				self.tree[prev].right = right
			else:
				while right is not None and self.tree[right].rank.geometric_rank > self.tree[left].rank.geometric_rank:
					prev = right
					right = self.tree[right].right
				self.tree[prev].left = left
				
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
