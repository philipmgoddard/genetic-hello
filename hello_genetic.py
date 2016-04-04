import random
import string
import copy

class Chromosone:
  '''
  Represents a chromosone
  '''

  def __init__(self, N):
    '''
    initialisation method for Chromosone.
    is a string of length N
    '''
    tmp = ''.join(
      random.SystemRandom().choice(
      string.ascii_uppercase +
      string.ascii_lowercase +
      string.digits +
      " "
    ) for _ in range(N))

    self.value = tmp



  def __str__(self):
    '''
    representation of Chromosone instance.
    just print string.
    '''
    return(self.value)



  def cost(self, objective):
    '''
    method to calculate cost.
    in this case, other should be a chromosone
    that represents the desired solution
    '''
    cost = 0
    for i in range(len(objective)):
      cost += (ord(objective[i]) - ord(self.value[i])) ** 2
    return(cost)



  def combine(self, other, position):
    '''
    method to combine two chromosones
    at specified position
    remember is not pure so it modifies self
    '''
    self.value = self.value[:position] + other.value[position:]



class Population:
  '''
  represents a population of chromosones
  '''
  mutate_prob = None
  pop_size = None
  objective = None



  def __init__(self, objective, pop_size = 100, mutate_prob = 0.02):
    self.objective = objective
    self.pop_size = pop_size
    self.mutate_prob = mutate_prob
    self.pool = []
    for i in range(self.pop_size):
      tmp = Chromosone(len(objective))
      self.pool.append(tmp)



  def __str__(self):
    res = []
    for chromosone in self.pool:
      res.append(
        str(chromosone) +
        " " +
        str(chromosone.cost(self.objective))
      )
    return('\n'.join(res) + '\n')


  def order(self):
    '''
    order method: arrange chromosones in pool from
    best to worst
    '''
    fitness = dict()
    for chromosone in self.pool:
      fitness[chromosone] = chromosone.cost(self.objective)

    tmp = list()
    for k, v in fitness.items():
      tmp.append((v, k))

    tmp.sort(key = lambda x: x[0])

    # now can order best to worst
    for i in range(self.pop_size):
      self.pool[i] = tmp[i][1]


  def breed(self, topN = 20):
    '''
    breed method: relies on chromosone combine
    method.
    '''
    tmp = copy.copy(self.pool[:(topN - 1)])

    for i in range(self.pop_size):
      random.shuffle(tmp)
      parent1 = copy.copy(tmp[0])
      parent2 = copy.copy(tmp[1])
      split = random.randint(1, (len(self.objective) - 1) )

      parent1.combine(parent2, split)
      self.pool[i] = copy.copy(parent1)



  def mutate(self):
    '''
    mutate method: if uniform random number less than
    mutat_prob, we will select one index at random
    and replace with random string from character set
    '''
    for i in range(self.pop_size):
      if(random.uniform(0, 1) < self.mutate_prob):
        index = random.randrange(len(self.objective))

        tmp = copy.copy(self.pool[i])
        stringList = list(tmp.value)
        stringList[index] = random.SystemRandom().choice(
          string.ascii_uppercase +
          string.ascii_lowercase +
          string.digits +
          " "
        )
        self.pool[i].value = ''.join(stringList)



def main():


  objective = ("Hello World")
  pop = Population(objective)
  #pop.order()

  #print(pop)

  print('# gen   cost     value')
  for i in range(5001):

    if(pop.pool[0].cost(objective) == 0):
      print('{:5d} {:6d}     {}'.format(
        i, pop.pool[0].cost(objective), pop.pool[0])
      )
      break

    if (i % 10) == 0:
      print('{:5d} {:6d}     {}'.format(
        i, pop.pool[0].cost(objective), pop.pool[0])
      )


    pop.breed()
    pop.mutate()
    pop.order()



if __name__ == "__main__":
  main()
