# CS6360_Assignment2
This is coding assignment for CS6360 dealing with bayesian networks. 

All of the answers can be found in `assignment2.ipynb`. It was designed as a notebook to make it easier to see computational answers alongside written answers to the various problems. 

An example call of the algorithm to find the query, for example, **P(Fraud|FP=T,IP=F,CRP=T)** is
```
answer = inference(factorList=factorList,
                   queryVariables=['Fraud'],
                   orderedListOfHiddenVariables=['Trav', 'OC'],
                   evidenceList={'FP': True, 'IP': False, 'CRP': True})
```
