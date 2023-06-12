import numpy as np


def calculate(list):
  # raise exception if not allowed format 
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  # transform list to 3x3 np array
  np_list = np.array(list).reshape(3,3)

  #calculate mean [axis=0, axis=1, flattened]
  mean = [(np.mean(np_list, axis=0)).tolist(), (np.mean(np_list, axis=1)).tolist(), np.mean(np_list)] 
  #calculate variance [axis=0, axis=1, flattened]
  variance = [(np.var(np_list, axis=0)).tolist(), (np.var(np_list, axis=1)).tolist(), np.var(np_list)]
  #calculate deviation [axis=0, axis=1, flattened]
  deviation = [(np.std(np_list, axis=0)).tolist(), (np.std(np_list, axis=1)).tolist(), np.std(np_list)]
  #calculate max [axis=0, axis=1, flattened]
  max = [(np.max(np_list, axis=0)).tolist(), (np.max(np_list, axis=1)).tolist(), np.max(np_list)]
  #calculate min [axis=0, axis=1, flattened]
  min = [(np.min(np_list, axis=0)).tolist(),(np.min(np_list, axis=1)).tolist(), np.min(np_list)]
  #calculate sum [axis=0, axis=1, flattened]
  sum = [(np.sum(np_list, axis=0)).tolist(),(np.sum(np_list, axis=1)).tolist(), np.sum(np_list)]
  #store calculated value in a dict
  calculations = {  
    'mean': mean,
    'variance': variance,
    'standard deviation': deviation,
    'max': max,
    'min': min,
    'sum': sum
  }
  # return dictionary with values
  return calculations
