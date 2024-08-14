### Addendum
We have not covered, at all, one further critical part of using Python - whether through a script or a Jupyter notebook. That is: making your own package. One use of this is to move some functions you write into a ```.py``` you can import, instead of defining locally in a notebook or scripte. Here are a couple of resources for how to do this:
- [A simple tutorial](https://www.pythoncentral.io/how-to-create-a-python-package/)
- [More complete guide](https://data-flair.training/blogs/python-packages/)
The simplest way, i think, is to: 
1. find the site-packages folder for the environment you want to use the package from
2. make a folder in there. The name of this folder will be the name of your package (e.g., ```/Users/danieljdenman/opt/anaconda3/envs/NSPbootcamp/lib/python3.8/site-packages/neuroscience``` will make a package called ```neuroscience```). 
3. add a file (it can have nothing written in it) called ```__init__.py```
4. from there, you can ```import neuroscience``` from wherever you want. the functions and variables within ```neuroscience``` will be available as ```neuroscience.function()``` or ```neuroscience.variable_name```
