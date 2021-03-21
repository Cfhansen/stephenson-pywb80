###solution to exercise 80 from ben stephenson's "the python workbook".

import random

def trial(): 

  results = []
  ok = False

  while ok == False:
    num = random.randint(1,2)
    if num == 1:
      results.append('H')
    else:
      results.append('T')

    if len(results) > 2:
      if (results[-1:] == results[-2:-1]) and (results[-1:] == results[-3:-2]):
        ok = True
        print(results)
        print(f'{len(results)} flips were needed.')
        return(len(results))

total_trials = 0
for i in range(1,1001):
  total_trials += trial()

print(f'On average {total_trials / 1000} flips were needed.')
