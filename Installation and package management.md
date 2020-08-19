# Installation and package management

We have installed Anaconda. This is a package management system, which helps us [install packages and create and maintain separate environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) for separate programming tasks. One of the great things about python is that we can leverage all of that public and free code out there. Great! One disadvantage: not everyone in the world has coordinated their code bases to work with everyone else's 🤼‍♂️ 🤺 🖥.. (ha!) this means that Jane's very_useful_package may require a numpy version that conflicts with Bob's pretty_good_tool. The solution: create seprate environments for working with Jane's very_useful_package and Bob's pretty_good_tool. For science, examples include separate environments for image analysis, Arduino control, a course, and a home project for scraping data from twitter. 

### Confirm you have created an Anaconda environment called NSPbootcamp
#### run the following line:
If the installation worked, after re-starting your Terminal/shell you should see:
<br> ```(base) username $```

#### good work! we're now going to create an environment and install packages together.
First, make sure you are in the NSPbootcamp directory
```conda create -n NSPbootcamp python=3.7```<br>
```conda activate NSPbootcamp```

### Add all of the needed packages to NSPbootcamp
There are a few different ways to add pacakges to your environment. In an Anaconda environment, choice A is to use: ```conda install name_of_my_package```. This depends on the package having an Anaconda channel. lot's of packages do. but some don't, in which case they almost certainly have a PyPi channel, in which case you need to use ```pip install name_of_my_package```.

#### here's another key element of how we'll use python: Jupyter Lab, for Jupyter ipython notebooks. let's install it: 
```conda install jupyterlab```<br>
When you install with ```conda install``` or ```pip install```, it'll have you confirm your intentions. go ahead and enter ```y``` and press ```enter```

#### we could keep going like this, one package at a time. but we can also do a bunch at once (note we could have also done this when we created the environment, but we are learning here!)
```conda install scipy seaborn scikit-image fsspec```

### finally, let's do a pip line to install a couple of things that aren't on Anaconda: 
```pip install gcsfs scanpy[louvain] allensdk==2.0.0```
<br>
there seems to be an issue with the allensdk versioning right now, so we also need one more line to clean up versions. (the ```-U``` flag here is telling ```pip``` to upgrade something that might already be installed):
<br> ```pip install -U pynwb hdmf```

### We should be good for the next couple of days of python fun!. 
Of course, we can always add packages later as we need them, using a terminal and ```conda install name_of_my_package```or ```pip install name_of_my_package```

### One more thing - a code editor. 
Choosing an editor is a personal choice that can generate strong opinions. [There are many options](https://duckduckgo.com/?q=best+python+code+editor). If you don't already have a strong preference, we'll use a fully featured and very popular one, VS Code. [Download and install it.](https://code.visualstudio.com/)
