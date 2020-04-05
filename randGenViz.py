import networkx as nx 
import matplotlib.pyplot as plt 
import random
from brent import brenter
from randGen import genSet, mapper

posNums = 1000
sampleSize = 1000
numIters = 30

#iterate over x number of random sets & functions, find largest cycle (lambda), and print graph for that function
lrg_lam = 0
lrg_mu = 0
lrg_fn = {}
lrg_x0 = 0
for i in range(numIters):
    numSet = genSet(posNums, sampleSize)
    fn = mapper(numSet)
    x0 = numSet[random.randint(0,len(numSet)-1)]
    lam, mu = brenter(fn, x0)
    if lam > lrg_lam:                       #find largest Cycle of every randomized function+sample
        lrg_lam = lam
        lrg_fn = fn 
        lrg_x0 = x0
        lrg_mu = mu
    
print('Function Map f(x):',lrg_fn)
print('Random Start Value (x.0):',lrg_x0)
print('Cycle Length (Lambda):',lrg_lam)
print('Start Index of Cycle (Mu):',lrg_mu)

cycle = []                          #print largest cycle
for z in range((lrg_lam+lrg_mu)+1):
    if z >= lrg_mu:
        cycle.append(lrg_x0)
    lrg_x0 = lrg_fn[lrg_x0]
print('Cycle:', cycle)

#create graph
plt.figure(figsize=(20,20))
G = nx.Graph() 
#add list of nodes to graph
G.add_nodes_from(list(lrg_fn.keys()))
G.add_edges_from(list(lrg_fn.items()))
nx.draw(G, with_labels=True, font_size=10)
plt.savefig('plot_path.png')
#plt.show()