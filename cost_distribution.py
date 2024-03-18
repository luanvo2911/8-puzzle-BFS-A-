import matplotlib.pyplot as plt
import numpy as np

from run_test import BFS_test, A_test

def average(array):
  length = len(array)
  total = sum(array)
  return round(total / length, 3)
    


if __name__ == '__main__':
  # BFS_test_pass, BFS_node_generated = BFS_test(100)
  # A_test_pass, A_node_generated = A_test(100)
  
  
  
  A_test_pass, A_node_generated = (2, [0, 0, 0, 3679, 0, 0, 0, 0, 0, 545])
  BFS_test_pass, BFS_node_generated = (2, [0, 0, 0, 278597, 0, 0, 0, 0, 0, 9083])
  
  average_A_node_generated = average(list(filter(lambda x: x > 0, A_node_generated)))
  average_BFS_node_generated = average(list(filter(lambda x: x > 0, BFS_node_generated)))
  
  Labels = ['BFS', 'A*']
  
  plt.subplot(1,2,1)
  
  plt.bar(0, np.array([average_BFS_node_generated]), width = 0.1, color='navy', label='BFS')
  plt.bar(1, np.array([average_A_node_generated]), width = 0.1, color='black', label='A*')
  
  plt.text(0, average_BFS_node_generated, average_BFS_node_generated)
  plt.text(1, average_A_node_generated, average_A_node_generated)
  
  plt.legend(('BFS', 'A*'))
  plt.xlabel('Types of algorithm')
  plt.xticks(range(2), labels = Labels)
  plt.ylabel('Node generated')
  plt.title('Comparison in node generated between BFS and A*')
  
  
  plt.subplot(1,2,2)
  
  plt.bar(0, np.array([BFS_test_pass]), width = 0.1, color='navy', label='BFS')
  plt.bar(1, np.array([A_test_pass]), width = 0.1, color='black', label='A*')
  
  plt.text(0, BFS_test_pass, BFS_test_pass)
  plt.text(1, A_test_pass, A_test_pass)
  
  plt.legend(('BFS', 'A*'))
  plt.xlabel('Types of algorithm')
  plt.xticks(range(2), labels = Labels)
  plt.ylabel('Number of test passed')
  plt.title('Comparison in testcase passed between BFS and A*')
  
  
  plt.suptitle('Comparison between BFS and A* through 1000 testcases', fontsize = 25)
  
  plt.show()
  
  
  # print(round(average([1988,4556,1234]), 3))
  
  
  