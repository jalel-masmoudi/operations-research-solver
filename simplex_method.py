"""
Simplex Method for Linear Programming
Solves: Maximize/Minimize c^T * x subject to Ax <= b, x >= 0
Time: O(2^n) worst case, polynomial average
"""

import numpy as np
from typing import Tuple, Dict

class SimplexSolver:
    def __init__(self, verbose=False):
        self.verbose = verbose
    
    def solve(self, c, A, b, maximize=True):
        """
        Solve LP problem using Simplex
        
        Args:
            c: Cost coefficients (to minimize)
            A: Constraint matrix (m x n)
            b: Right-hand side (m,)
            maximize: True to maximize, False to minimize
        
        Returns:
            Dict with: optimal_value, solution, status, iterations
        """
        if maximize:
            c = -c  # Convert maximization to minimization
        
        # Convert to standard form by adding slack variables
        m, n = A.shape
        A_std = np.hstack([A, np.eye(m)])
        c_std = np.hstack([c, np.zeros(m)])
        
        # Initial tableau
        # [A | I | b]
        # [c | 0 | 0]
        tableau = np.hstack([A_std, b.reshape(-1, 1)])
        cost_row = np.hstack([c_std, ])
        
        tableau = np.vstack([tableau, cost_row])
        
        iterations = 0
        
        while True:
            iterations += 1
            
            # Check if optimal (all costs >= 0)
            if np.all(tableau[-1, :-1] >= -1e-10):
                break
            
            # Find entering variable (most negative cost)
            entering = np.argmin(tableau[-1, :-1])
            
            # Find leaving variable (minimum ratio test)
            ratios = []
            for i in range(m):
                if tableau[i, entering] > 1e-10:
                    ratio = tableau[i, -1] / tableau[i, entering]
                    ratios.append((ratio, i))
                else:
                    ratios.append((np.inf, i))
            
     
