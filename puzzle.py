

class Puzzle:
  def __init__(self, node, threshold):
    pass
  def find_solution(self):
    pass
  def trace_path(node, num_of_test, type):
    f = open(f"./solution/{type}/{num_of_test}.txt", "w")
    print("Tracing back .....")
    result_list = []
    parent_node = node
    while parent_node:
      result_list.append(parent_node.action)
      parent_node = parent_node.parent
    
    result_list = result_list[::-1]
    for i in result_list:
      if(i):
        f.write(str(i) + "  ")
    f.close()
    print(result_list)
    return len(result_list) - 1