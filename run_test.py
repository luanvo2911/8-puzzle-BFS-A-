from puzzle_BFS import BFSSearch
from puzzle_A import ASearch

def read_file(x):
  f = open(f"./test/{x}.txt", "r")
  get_str = f.read()
  convert_arr = []
  for i in get_str:
    convert_arr.append(int(i))
  f.close()
  return convert_arr




def BFS_test(num_of_test):
  count_passed_BFS = 0
  count_failed_BFS = 0
  node_generated_array = list()
  
  for i in range(0, num_of_test):
    input = read_file(i)
    print(input)
    node_generated = BFSSearch(input, 500000).find_solution()
    if (node_generated):
        print(f"Test case {i}: passed")
        print(f"Node generated: {node_generated}")
        count_passed_BFS += 1
        node_generated_array.append(node_generated)
    else:
        print(f"Test case {i}: failed")
        count_failed_BFS += 1
        node_generated_array.append(0)
        
  return count_passed_BFS, node_generated_array



def A_test(num_of_test):
  count_passed_A = 0
  count_failed_A = 0
  node_generated_array = list()
  
  for i in range(0, num_of_test):
    input = read_file(i)
    print(input)
    node_generated = ASearch(input, 200000).find_solution()
    if (node_generated):
        print(f"Test case {i}: passed")
        print(f"Node generated: {node_generated}")
        count_passed_A += 1
        node_generated_array.append(node_generated)
    else:
        print(f"Test case {i}: failed")
        count_failed_A += 1
        node_generated_array.append(0)
        
  return count_passed_A, node_generated_array
        
# print("\n Overall: \n")
# print("\n BFS Search \n")
# print(f"Passed cases: {count_passed_BFS} cases")
# print(f"Failed cases: {count_failed_BFS} cases")

# print("\n A* Search \n")
# print(f"Passed cases: {count_passed_A} cases")
# print(f"Failed cases: {count_failed_A} cases")
  
  




