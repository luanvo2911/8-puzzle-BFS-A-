from collections import deque
from Node import Node

  
class BFSSearch:
  def __init__ (self, node, threshold):
    self.node = Node(node)
    self.explored = deque([self.node]) ## opened list
    self.traversed = set() ## closed list
    self.goal = Node([0,1,2,3,4,5,6,7,8])
    self.count = 1 # count generated node
    self.threshold = threshold
  
  def find_solution(self):
    # is_goal = False
    if self.node == self.goal:
      return []

    while self.explored and self.count < self.threshold:
      current_node = self.explored.popleft()
      self.traversed.add(current_node)
      for n in current_node.get_children():
        if(n not in self.traversed):
          if n == self.goal:
            # print("Found solution !!")
            # print(f"Generated states: {self.count} states")
            # BFSSearch.trace_path(n)
            return self.count
          self.explored.append(n)
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
   
    
# # n = Node([1,2,4,3,0,5,7,6,8])
# n = [1,8,2,0,4,3,7,6,5]
# # n = Node([1,0,2,3,4,5,6,7,8])
# search = BFSSearch(n).find_solution()