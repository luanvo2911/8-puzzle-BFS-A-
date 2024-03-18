class Node:
  
  def __init__ (self, state, action = None, parent = None):
    self.state = tuple(state) # 1-dimensional array 9 elements
    self.action = action
    self.parent = parent
    ## below var is used for A*
    if parent is not None:
      self.g_score = parent.g_score + 1
    else:
      self.g_score = 0
    self.h_score = self.get_h_score()
      
  def __eq__(self, other):
    if other == None:
      return None
    return self.state == other.state

  def __lt__(self, other): ## compare in priority queue
    if other == None:
      return None
    return self.g_score + self.h_score < other.g_score + other.h_score ## compare f_score between 2 state

  def __str__(self):
    string = '\n'
    for i in range(0, 3):
      for j in range(0, 3):
        string += str(self.state[3 * i + j]) + "  "
      string += "\n" if i < 2 else ""
    return string

  def __hash__(self):
        return hash(self.state)
  
  def get_blank_position(state):
    for i in range(0, 9):
      if(state[i] == 0):
        return i
  
  def get_h_score(self): ## using manhattan algorithm
    h_score = 0
    for i in range(0, 9):
      h_score += abs(int(self.state[i] / 3) - int(i / 3)) + abs(self.state[i] % 3 - i % 3)
    return h_score
      
  
  def move_left(self):
    return_state = [x for x in self.state]
    blank_position = Node.get_blank_position(return_state)
    if(blank_position % 3 < 2):
      return_state[blank_position], return_state[blank_position + 1] = return_state[blank_position + 1], return_state[blank_position]
      return return_state
    return None
  
  def move_right(self):
    return_state = [x for x in self.state]
    blank_position = Node.get_blank_position(return_state)
    if (blank_position % 3 > 0):
      return_state[blank_position], return_state[blank_position - 1] = return_state[blank_position - 1], return_state[blank_position]
      return return_state
    return None
  
  def move_up(self):
    return_state = [x for x in self.state]
    blank_position = Node.get_blank_position(return_state)
    if(int(blank_position / 3) < 2):
      return_state[blank_position], return_state[blank_position + 3] = return_state[blank_position + 3], return_state[blank_position]
      return return_state
    return None
  
  def move_down(self):
    return_state = [x for x in self.state]
    blank_position = Node.get_blank_position(return_state)
    if(int(blank_position / 3) > 0):
      return_state[blank_position], return_state[blank_position - 3] = return_state[blank_position - 3], return_state[blank_position]
      return return_state
    return None
  
  def get_children(self):
    children_list = []
    
    children_down = Node.move_down(self)
    children_up = Node.move_up(self)
    children_left = Node.move_left(self)
    children_right = Node.move_right(self)

    if(children_down):
      children_list.append(Node(children_down, 'D', self))
    if(children_up):
      children_list.append(Node(children_up, 'U', self))
    if(children_left):
      children_list.append(Node(children_left, 'L', self))
    if(children_right):
      children_list.append(Node(children_right, 'R', self))
      
    return children_list
  
  
  
# n = Node([1, 2, 0, 3, 4, 5, 6, 7, 8])

# print(n.h_score)
# print(n.g_score)