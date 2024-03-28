import numpy as np

class VarElim:
    def __init__(self) -> None:
        pass
    

    # Implementation for restrictedFactor = restrict(factor, variable, value)
    # Function that restricts a variable to some value in a given factor
    def restrict(self,factor,variable,value):
        return None
    

    # Implementation for productFactor = multiply(factor1, factor2)
    def multiply(self,factor1,factor2):
        return None
    

    # Implementation for resultFactor = sumout(factor, variable):
    def sumout(self,factor,variable):
        return None
    
    
    # Implementation for normalizedFactor = normalize(factor):
    def normalize(self,factor):
        return None
    

    # Implementation for resultFactor = inference(factorList, queryVariables, orderedListOfHiddenVariables, evidenceList)
    def inference(self, factorList, queryVariables, orderedListOfHiddenVariables,evidenceList):
        return None