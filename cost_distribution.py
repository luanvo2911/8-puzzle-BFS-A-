import matplotlib.pyplot as plt
import numpy as np

from run_test import BFS_test, A_test

def average(array):
  length = len(array)
  total = sum(array)
  return round(total / length, 3)
    


if __name__ == '__main__':
  num_of_testcases = 1000
  
  BFS_test_pass, BFS_node_generated, BFS_path_cost = BFS_test(num_of_testcases)
  A_test_pass, A_node_generated, A_path_cost = A_test(num_of_testcases)
  
  average_A_node_generated = average(list(filter(lambda x: x > 0, A_node_generated)))
  average_BFS_node_generated = average(list(filter(lambda x: x > 0, BFS_node_generated)))
  average_A_path_cost = average(list(filter(lambda x: x> 0, A_path_cost)))
  average_BFS_path_cost = average(list(filter(lambda x: x> 0, BFS_path_cost)))
  
  
  Labels = ['BFS', 'A*']
  
  plt.subplot(221)
  
  plt.bar(0, np.array([average_BFS_node_generated]), width = 0.1, color='navy', label='BFS')
  plt.bar(1, np.array([average_A_node_generated]), width = 0.1, color='black', label='A*')
  
  plt.text(0, average_BFS_node_generated, str(average_BFS_node_generated))
  plt.text(1, average_A_node_generated, str(average_A_node_generated))
  
  plt.legend(('BFS', 'A*'))
  plt.xlabel('Types of algorithm')
  plt.xticks(range(2), labels = Labels)
  plt.ylabel('Node generated')
  plt.title('Comparison in average node generated between BFS and A*')
  
  
  plt.subplot(222)
  
  plt.bar(0, np.array([BFS_test_pass]), width = 0.1, color='navy', label='BFS')
  plt.bar(1, np.array([A_test_pass]), width = 0.1, color='black', label='A*')
  
  plt.text(0, BFS_test_pass, str(BFS_test_pass))
  plt.text(1, A_test_pass, str(A_test_pass))
  
  plt.legend(('BFS', 'A*'))
  plt.xlabel('Types of algorithm')
  plt.xticks(range(2), labels = Labels)
  plt.ylabel('Number of test passed')
  plt.title('Comparison in testcase passed between BFS and A*')
  
  plt.subplot(223)
  
  plt.bar(0, np.array([average_BFS_path_cost]), width = 0.1, color='navy', label='BFS')
  plt.bar(1, np.array([average_A_path_cost]), width = 0.1, color='black', label='A*')
  
  plt.text(0, average_BFS_path_cost, str(average_BFS_path_cost))
  plt.text(1, average_A_path_cost, str(average_A_path_cost))
  
  plt.legend(('BFS', 'A*'))
  plt.xlabel('Types of algorithm')
  plt.xticks(range(2), labels = Labels)
  plt.ylabel('Node generated')
  plt.title('Comparison in average path cost between BFS and A*')
  
  
  plt.suptitle('Comparison between BFS and A* through 1000 testcases', fontsize = 25)
  
  plt.show()
  
  
  