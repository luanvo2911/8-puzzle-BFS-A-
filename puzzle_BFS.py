from collections import deque
from Node import Node
from puzzle import Puzzle
  
class BFSSearch(Puzzle):
  def __init__ (self, node, threshold, num_of_test):
    self.node = Node(node)
    self.explored = deque([self.node]) ## opened list
    self.traversed = set() ## closed list
    self.goal = Node([0,1,2,3,4,5,6,7,8])
    self.count = 1 # count generated node
    self.threshold = threshold
    self.num_of_test = num_of_test
  
  def find_solution(self):
    # is_goal = False
    if self.node == self.goal:
      return 0, 0

    while self.explored and self.count < self.threshold:
      current_node = self.explored.popleft()
      self.traversed.add(current_node)
      for n in current_node.get_children():
        if(n not in self.traversed):
          if n == self.goal:
            path_cost = BFSSearch.trace_path(n, self.num_of_test, "BFS")
            return self.count, path_cost
          self.explored.append(n)
          self.count += 1
    print(f"After generating {self.count} states, cannot find solutions")
    return None, None