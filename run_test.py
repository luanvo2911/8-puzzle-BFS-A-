from puzzle_BFS import BFSSearch
from puzzle_A import ASearch

def read_file(x):
  f = open(f"./test/{x}.txt", "r")
  get_str = f.read()
  convert_arr = []
  str_out = ""
  for i in range(len(get_str)):
    convert_arr.append(int(get_str[i]))
    str_out += get_str[i]
    if(i%3 == 2):
      str_out += "\n"
  f.close()
  return convert_arr, str_out




def BFS_test(num_of_test):
  count_passed_BFS = 0
  count_failed_BFS = 0
  node_generated_array = list()
  path_costs_array = list()
  
  for i in range(0, num_of_test):
    input, str_out = read_file(i)
    print(str_out)
    node_generated, path_cost = BFSSearch(input, 500000, i).find_solution()
    if (node_generated):
        print(f"Test case {i}: passed")
        print(f"Node generated: {node_generated}")
        print(f"Path cost: {path_cost}")
        count_passed_BFS += 1
        node_generated_array.append(node_generated)
        path_costs_array.append(path_cost)
    else:
        print(f"Test case {i}: failed")
        count_failed_BFS += 1
        node_generated_array.append(0)
        path_costs_array.append(0)
        
  return count_passed_BFS, node_generated_array, path_costs_array



def A_test(num_of_test):
  count_passed_A = 0
  count_failed_A = 0
  node_generated_array = list()
  path_costs_array = list()
  
  for i in range(0, num_of_test):
    input, str_out = read_file(i)
    print(str_out)
    node_generated, path_cost = ASearch(input, 200000, i).find_solution()
    if (node_generated):
        print(f"Test case {i}: passed")
        print(f"Node generated: {node_generated}")
        count_passed_A += 1
        node_generated_array.append(node_generated)
        path_costs_array.append(path_cost)
    else:
        print(f"Test case {i}: failed")
        count_failed_A += 1
        node_generated_array.append(0)
        path_costs_array.append(0)
        
  return count_passed_A, node_generated_array, path_costs_array
        
# print("\n Overall: \n")
# print("\n BFS Search \n")
# print(f"Passed cases: {count_passed_BFS} cases")
# print(f"Failed cases: {count_failed_BFS} cases")

# print("\n A* Search \n")
# print(f"Passed cases: {count_passed_A} cases")
# print(f"Failed cases: {count_failed_A} cases")
  
  




