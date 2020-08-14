## Scripts 
#### Yesterday, we used Jupyter Lab to do some data exploration and analysis in a Jupyter notebook. 
This is a very efficient way to do data exploration, analysis, and figure making. But there are certainly cases where you want the computer to run something in the background, or execute one thing and be done. In these cases, you might opt for writing a python script, a ```.py``` file that you can invoke from the command line. 

#### This morning, we will make a script from scratch that interacts with an Arduino board with a joystick. 
This is an example of how one might use a script - as a the logical control for a behavioral task an animal is performing (i.e., interacting with the joystick). We are making a video game. Other good uses of scripts in the lab are moving data around the network in an automated way; standalone scripts that regenerate a figure based on updated data (similar to the FluorescenceAnalysis Jupyter notebook we made yesterday). There are plenty more. While doing so, we will go over more flow control (loops, conditional statements) and object-oriented programming. 

Step 1: open VS Code. 

Let's take a look at what we have here:
![vs code]('../res/vscode1.png')
We have a window where we can write code. We have some bells and whistles, like a terminal that lives right here with us in VS code if we need to do terminal things. More useful features will appear as we make our script. 

We have not covered, at all, one further critical part of using Python - whether through a script or a Jupyter notebook. That is: making your own package. One use of this is to move some functions you write into a ```.py``` you can import, instead of defining locally in a notebook or scripte. Here are a couple of resources for how to do this:
- [A simple tutorial](https://www.pythoncentral.io/how-to-create-a-python-package/)
- [More complete guide](https://data-flair.training/blogs/python-packages/)
The simplest way, i think, is to: 
1. find the site-packages folder for the environment you want to use the package from
2. make a folder in there. The name of this folder will be the name of your package (e.g., ```/Users/danieljdenman/opt/anaconda3/envs/NSPbootcamp/lib/python3.8/site-packages/neuroscience``` will make a package called ```neuroscience```). 
3. add a file (it can have nothing written in it) called ```__init__.py```
4. from there, you can ```import neuroscience``` from wherever you want. the functions and variables within ```neuroscience``` will be available as ```neuroscience.function()``` or ```neuroscience.variable_name```
