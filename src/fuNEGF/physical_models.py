# split the LinearChain in 'models.py' into a generic superclass 'System' containing a blueprint with all the NEGF routines, while the linear chain will be conveniently implemented in 'LinearChain' which will inherit from System

# first class called System will contain all the routines of a physical system with an NEGF solver
class System:
     raise NotImplementedError

