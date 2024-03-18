from queue import PriorityQueue
from Node import Node

class ASearch:
  def __init__(self, node, threshold):
    self.node = Node(node)
    self.explored = PriorityQueue() ## opened list
    self.traversed = set() ## closed list
    self.goal = Node([0,1,2,3,4,5,6,7,8])
    self.count = 1 # count generated node
    self.threshold = threshold
    
  def find_solution(self):
    if self.node == self.goal:
      return []
    self.explored.put(self.node)
    while self.explored and self.count < self.threshold:
      current_node = self.explored.get()
      self.traversed.add(current_node)
      for n in current_node.get_children():
        if(n not in self.traversed):
          if n == self.goal:
            # print("Found solution!!")
            # print(f"Generated states: {self.count} states")
            # ASearch.trace_path(n)
            return self.count
          self.explored.put(n)
          self.count += 1
    print(f"After generating {self.count} states, cannot find solutions")
    return None
  
  
  def trace_path(node):
    print("Tracing back .....")
    result_list = []
    parent_node = node
    while parent_node:
      result_list.append(parent_node)
      parent_node = parent_node.parent
    
    result_list = result_list[::-1]
    for i in result_list:
      print(f"move to {i.action}")   
      print(i)
      