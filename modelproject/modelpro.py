#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import optimize

import numpy as np
from scipy import interpolate
from scipy import linalg
from scipy import optimize
from types import SimpleNamespace
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

import numpy as np
from scipy.optimize import minimize

class malthus_economics:
    def __init__(self):
        # Setting values for parameters
        self.X = 100
        self.L = 20000  
        self.A = 1 
        self.alpha = 0.5  
        self.Lambda = 1  
        self.beta = 0.5 
        self.mu = 0.01
        self.tau = 0.4
        self.g = 0
        
    # Defining the utility function u = beta*log(c)+(1-beta)*log(n)
    def utility(self, x, beta):
        c, n = x # making a tuple which takes c and n values
        return beta * np.log(c) + (1 - beta) * np.log(n)

    # Define income per capita 
    def income(self, X, L, A, alpha):
        return ((A * X) / L) ** alpha

    def constraint1(self, x, y, Lambda, tau):
        c, n = x
        return np.array([
            y * (1 - tau) - c - Lambda * n,
        ])

    def maximize_utility(self, X, L, A, alpha, Lambda, beta, tau):
        y = self.income(X, L, A, alpha)
        x0 = np.array([y / 2 + 0.0001, 1])  # Initial guess for c and n
        bounds = ((0.0001, y), (0.0001, None))  # Bounds for c and n
        
        constraints = ({'type': 'ineq', 'fun': self.constraint1, 'args': (y, Lambda, tau)})
        res = minimize(lambda x: -self.utility(x, beta), x0, method='SLSQP', bounds=bounds, constraints=constraints)
        return res

    
       # Define population in next period 
    def next_period_population(self, L, n_optimal, mu):
        return n_optimal * L + (1 - mu) * L 

    # Define function for updating technology
    def technology_next_period(self):
        return self.A * (1 + self.g)

    def steady_state(self):
        tolerance = 1e-8
        max_iter = 1000
        n_optimal = 1
        population = [self.L]
        income_list = [self.income(self.X, self.L, self.A, self.alpha)]
        technology_list = [self.A]
        for i in range(max_iter):
        
            res = self.maximize_utility(self.X, self.L, self.A, self.alpha, self.Lambda, self.beta, self.tau)
            n_optimal_new = res.x[1]
            L_new = self.next_period_population(self.L, n_optimal_new, self.mu)
            
            self.A= self.technology_next_period()
            if abs(L_new - self.L) < tolerance:
                break
            
            n_optimal = n_optimal_new
            self.L = L_new
            population.append(L_new)
            income_list.append(self.income(self.X, L_new, self.A, self.alpha))
            technology_list.append(self.A)
                   
                   
            

        # Print results
        print(f"Steady state population size: {self.L}")
        print(f"Optimal number of children: {n_optimal}")
        print(f"Steady state income: {self.income(self.X, self.L, self.A, self.alpha)}")

        

        # Create plot
        fig, axs = plt.subplots(2, 1, figsize=(10, 6))

        # Plot population and income
        axs[0].set_xlabel('Years')
        axs[0].set_ylabel('Population', color='tab:red')
        axs[0].plot(population, color='tab:red')
        axs[0].tick_params(axis='y', labelcolor='tab:red')

        axs_right = axs[0].twinx()  # Create a twin Axes sharing the x-axis
        axs_right.set_ylabel('Income', color='tab:blue')
        axs_right.plot(income_list, color='tab:blue')
        axs_right.tick_params(axis='y', labelcolor='tab:blue')

        # Plot technology
        axs[1].set_xlabel('Years')
        axs[1].set_ylabel('Technology', color='tab:green')
        axs[1].plot(technology_list, color='tab:green')
        axs[1].tick_params(axis='y', labelcolor='tab:green')

        fig.tight_layout()
        plt.show()

        

    def steady_state1(self):
        tolerance = 1e-8
        max_iter = 1000
        n_optimal = 1
        population = [self.L]
        income_list = [self.income(self.X, self.L, self.A, self.alpha)]
        technology_list = [self.A]
        for i in range(max_iter):
            if i == 100:
                self.A = 2
            res = self.maximize_utility(self.X, self.L, self.A, self.alpha, self.Lambda, self.beta, self.tau)
            n_optimal_new = res.x[1]
            L_new = self.next_period_population(self.L, n_optimal_new, self.mu)
            
            self.A= self.technology_next_period()
            if abs(L_new - self.L) < tolerance:
                break
            
            n_optimal = n_optimal_new
            self.L = L_new
            population.append(L_new)
            income_list.append(self.income(self.X, L_new, self.A, self.alpha))
            technology_list.append(self.A)
  

        # Print results
        print(f"Steady state population size: {self.L}")
        print(f"Optimal number of children: {n_optimal}")
        print(f"Steady state income: {self.income(self.X, self.L, self.A, self.alpha)}")

        

        # Create plot
        fig, axs = plt.subplots(2, 1, figsize=(10, 6))

        # Plot population and income
        axs[0].set_xlabel('Years')
        axs[0].set_ylabel('Population', color='tab:red')
        axs[0].plot(population, color='tab:red')
        axs[0].tick_params(axis='y', labelcolor='tab:red')

        axs_right = axs[0].twinx()  # Create a twin Axes sharing the x-axis
        axs_right.set_ylabel('Income', color='tab:blue')
        axs_right.plot(income_list, color='tab:blue')
        axs_right.tick_params(axis='y', labelcolor='tab:blue')

        # Plot technology
        axs[1].set_xlabel('Years')
        axs[1].set_ylabel('Technology', color='tab:green')
        axs[1].plot(technology_list, color='tab:green')
        axs[1].tick_params(axis='y', labelcolor='tab:green')

        fig.tight_layout()
        plt.show()

