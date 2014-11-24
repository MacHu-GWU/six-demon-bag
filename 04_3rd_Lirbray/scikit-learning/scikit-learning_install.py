'''
All the following package can be download from:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/
Dependency
|--- Scikit-learning 0.15
        Scikit-learning integrates classic machine learning algorithms. Requires Numpy-MKL
        |--- Scipy >= 0.7
            SciPy is software for mathematics, science, and engineering. Requires Numpy-MKL
            |--- Numpy-MKL 1.8
                NumPy is a fundamental package needed for scientific computing with Python.
            |--- Sympy 0.7.5
                Sympy is a library for symbolic mathematics
            |--- Pandas 0.14.0
                Pandas is a cross-section and time series data analysis toolkit.
                |--- openpyxl 1.8.5
                    openpyxl is a open python excel package (pip install openpyxl == 1.8.5)
                    Because Pandas need openpyxl to IO excel, and display excel table.
                    But it only support range(1.6.2, 2.0.1). So 1.8.5 is the best choice.
            |--- Matplotlib 1.3.1
                Matplotlib is a 2D plotting library
'''