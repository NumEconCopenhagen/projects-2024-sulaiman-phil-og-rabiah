from types import SimpleNamespace
import numpy as np
from scipy import optimize
class ExchangeEconomyClass:

    def __init__(self):

        par = self.par = SimpleNamespace()

        # Setting preferences references
        par.alpha = 1/3
        par.beta = 2/3

        # Determine endowments
        par.w1A = 0.8
        par.w2A = 0.3
        
        # Parameters to be valued later
        sol = self.sol = SimpleNamespace()
        sol.x1 = np.nan
        sol.x2 = np.nan
        sol.u = np.nan
        sol.p = np.nan
    
    def utility_A(self,x1A,x2A):
        '''Utility function for consumer A dependent on good 1 and 2'''
        return x1A**par.alpha*x2A**(1-self.par.alpha)
    def utility_B(self,x1B,x2B):
        return x1B**self.par.beta*x2B**(1-self.par.beta)

    
    def demand_A(self, p1):
        x1A = self.par.alpha * ((p1 * self.par.w1A + self.par.w2A) / p1)
        x2A = (1 - self.par.alpha) * (p1 * self.par.w1A + self.par.w2A)
        return x1A, x2A 
    
    def demand_B(self, p1):
        par = self.par
        x1B = self.par.beta*((p1*(1-self.par.w1A)+(1-self.par.w2A))/p1)
        x2B = (1-self.par.beta)*((p1*(1-self.par.w1A)+(1-self.par.w2A)))
        return x1B, x2B
    
    def check_market_clearing(self,p1):

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2
    
    def pareto(self, x1A, x2A):
        par = self.par
        pareto = []
        init_utilityA = self.utility_A(par.w1A, par.w2A)
        init_utilityB = self.utility_B(1 - par.w1A, 1 - par.w2A)
        for i, c in enumerate(x1A):
            for j, d in enumerate(x2A):
                if self.utility_A(c, d) >= init_utilityA and self.utility_B(1 - c, 1 - d) >= init_utilityB:
                    pareto.append((c, d))
        return pareto
    
    
    def solve_A(self):
  
        
        # Function for minimization 
        obj = lambda p1: -self.utility_A(1 - self.demand_B(p1)[0],1 - self.demand_B(p1)[1]) # minimize -> negative of utility
            
        # Constraints taking lowest value of 1*10^(-8)
        bounds = ((1e-8,None),)
                
        # Solver
        p10 = 1.5
        result = optimize.minimize(obj,p10,method='SLSQP',bounds=bounds)
            
        # Load
        p1opt = result.x[0]
        utilityA_opt = self.utility_A(self.demand_A(p1opt)[0],self.demand_A(p1opt)[1])
        return p1opt, utilityA_opt
    
    def solve_A_pareto(self):
        '''
        Solves the market maker problem for A by maximizing utility subject to a pareto improvement constraint for B.

        Returns:
        - p1opt (float): Optimal price of good 1 for agent A.
        - utilityA_opt (float): Optimal utility of agent A.
        '''
        par = self.par
 
        obj = lambda xA: -self.utility_A(xA[0],xA[1])
            
        budget_constraint = lambda xA: self.utility_B(1 - xA[0],1 - xA[1]) - self.utility_B(1 - par.w1A, 1 - par.w2A)
        constraints = ({'type':'ineq','fun':budget_constraint})
        bounds = ((1e-8,1),(1e-8,1))
                
       
        x0 = [0.2,0.8]
        result = optimize.minimize(obj,x0,method='SLSQP',constraints=constraints, bounds=bounds)
        x1Aopt, x2Aopt = result.x
        
        print(f'The consumption for A is: x1A  = {x1Aopt:.4f}, x2A = {x2Aopt:.4f}')
        print(f'The consumption for B is: x1B  = {1 - x1Aopt:.4f}, x2B = {1 - x2Aopt:.4f}')

        return x1Aopt, x2Aopt
    
    
    
    
    def solve_social_planner(self):
 
        obj = lambda xA: -(self.utility_A(xA[0],xA[1]) + self.utility_B(1 - xA[0],1 - xA[1]))
            

        bounds = ((1e-8,1),(1e-8,1))
                
        
        x0 = [0.5,0.5]
        result = optimize.minimize(obj,x0,method='SLSQP',bounds=bounds)
            
       
        x1Aopt, x2Aopt = result.x
        return x1Aopt, x2Aopt
    
    def solve_market_equilibrium(self, w1A):
        p1_eq = np.zeros(len(w1A))
        for i in range(len(w1A)):
            obj = lambda p1: self.demand_A(p1)[0]-w1A[i] + self.demand_B(p1)[0]-(1-w1A[i])
            res = optimize.root_scalar(obj,bracket=(1e-8,10),method='bisect')
            p1_eq[i] = res.root
        x1A_eq, x2A_eq = self.demand_A(p1_eq)
        X1B_eq, X2B_eq = self.demand_B(p1_eq)
        return x1A_eq, x2A_eq, X1B_eq, X2B_eq
    
    
      # Function that solves
    def solve(self, type="central"):
        par = self.par
        sol = self.sol

        if type == "central":
            obj_fun = lambda x: -(self.utility_A(x[0],x[1])+self.utility_B((1-x[0]),(1-x[1])))
            constraints = ({'type': 'ineq', 'fun': lambda x: x[0]-par.w1A+(1-x[0])-(1-par.w1A)})
        elif type == "mm":
            obj_fun = lambda x: -(self.utility_A(x[0],x[1])) 
            constraints = ({'type': 'ineq', 'fun': lambda x: x[0]-par.w1A+(1-x[0])-(1-par.w1A)},{'type': 'ineq', 'fun': lambda x: self.utility_B(1-x[0],1-x[1])-self.utility_B(1-par.w1A,1-par.w2A)})
        elif type == 'market':                                   
            obj_fun = lambda x: np.sum(np.abs(self.check_market_clearing(x)))
        else:
            print('no type chosen')
            
        if type == 'market':   
            initial_prices = [1.0]
            res = optimize.minimize(obj_fun, initial_prices, method='Nelder-Mead')
            # store results
            p1 = res.x[0]
            x1A, x2A = self.demand_A(p1)
            x1B, x2B = self.demand_B(p1)
            sol.p = p1
            sol.x1 = x1A
            sol.x2 = x2A
            sol.u = self.utility_A(x1A, x2A) + self.utility_B(x1B, x2B)

            print(f'x1A = {sol.x1:.3f} x2A = {sol.x2:.3f}, U_{type} = {sol.u:.3f}, u_A = {self.utility_A(sol.x1,sol.x2):.3f}, u_B = {self.utility_B(1-sol.x1,1-sol.x2):.3f}, p = {sol.p:.3f}')
        else:   
            initial_guess = [par.w1A,par.w2A]
            res = optimize.minimize(obj_fun,initial_guess,method='SLSQP',bounds=bounds,constraints=constraints)
            sol.x1 = res.x[0]
            sol.x2 = res.x[1]
            sol.u = -obj_fun((res.x[0],res.x[1]))
            print(f'x1A = {sol.x1:.3f} x2A = {sol.x2:.3f}, U_{type} = {sol.u:.3f}, u_A = {self.utility_A(sol.x1,sol.x2):.3f}, u_B = {self.utility_B(1-sol.x1,1-sol.x2):.3f}')