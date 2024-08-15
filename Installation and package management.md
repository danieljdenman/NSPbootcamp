# Installation and package management

# Installation
We will install a package management system, a code editor, and version control system. (For reference, as of 2023 installing MATLAB includes each of these, but with Python we do this separately.) 
- A package management system, which helps us [install packages and create and maintain separate environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) for separate programming tasks. We will now install Anaconda, do this. One of the great things about python is that we can leverage all of that public and free code out there. Great! One disadvantage: not everyone in the world has coordinated their code bases to work with everyone else's 🤼‍♂️ 🖥 🤺 . this means that Jane's very_useful_package may require a numpy version that conflicts with Bob's pretty_good_tool. The solution: create seprate environments for working with Jane's very_useful_package and Bob's pretty_good_tool. For science, examples might include separate environments for image analysis, Arduino control, for data analysis of RNAseq data, for analysis of Ca2+ imaging data....or even a course (like this one) or a home project scraping data from instagram.
- A code editor makes it a little prettier to write code and see outputs than it might be writing code in a blank unformatted document (which is also an option...)
- A version control system helps you get and share code with others. What's not to love, using code that other people wrote?

## A. Install Anaconda for package and environment management
[download](https://www.anaconda.com/products/individual) and [install](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) Anaconda.

## B. Install a code editor. 
Choosing an editor is a personal choice that can generate strong opinions. [There are many options](https://hackr.io/blog/best-python-ide). If you don't already have a strong preference, we'll use a fully featured and very popular one, VS Code. [Download and install it.](https://code.visualstudio.com/). If you do already have a strong preference, great! That means you know how to use it, but please be confirm you know how to use your editor with a git workflow, as this will be used to manage code work for the first year NSP courses. 

## C. Install git. 
Download and install git in your system using the official [website](https://git-scm.com/downloads). If you think you might already have git, open a terminal and confirm with `git -version`

## D. Create a Github account and link it to VS Code.
1. Go to [Github](https://www.github.com) and create an account. You can use any email you want including your anschutz.edu or a personal email. 
2. Configure VS Code to use your Github account. Open a VS code Terminal (press Ctrl+J or ⌘+J) and enter the below, one line at a time, replacing the "Your..." with your information. 
```
git config –global user.name “YourUserNameOnGithub”
```
```
git config –global user.email “YourEmail”
```

<br>
<br>
<br>

# Package Management
1. Open a command prompt - easiest to open a terminal in our newly installed VS Code (or use the Mac OS X program Terminal or on Windows the newly installed Anaconda command prompt). 
1. create a new environment. you should name your envirornment something short and informative about what it will be used for, e.g.: `NSPbootcamp`. <br> Use the command: ```conda create -n NSPbootcamp```  feel free to copy/paste  


### E. Confirm you have created an Anaconda environment called NSPbootcamp
1. run the following line:
<br>```conda activate NSPbootcamp```
2. success?
you should see ```(NSPbootcamp)``` before anything else on the new line of your Terminal/shell:
![shell screenshot](https://github.com/danieljdenman/NSPbootcamp/blob/master/res/activate_env.png)


### F. Add all of the needed packages to NSPbootcamp
There are a few different ways to add pacakges to your environment. In an Anaconda environment, choice A is to use: ```conda install name_of_my_package```. This depends on the package having an Anaconda channel. lot's of packages do. but some don't, in which case they almost certainly have a PyPi channel, in which case you need to use ```pip install name_of_my_package```.

#### here's another key element of how we'll use python: Jupyter Lab, for Jupyter ipython notebooks. let's install it: 
1. run the command ```conda install jupyterlab```<br>
When you install with ```conda install``` or ```pip install```, it'll have you confirm your intentions. go ahead and enter ```y``` and press ```enter```

#### we could keep going like this, one package at a time. but we can also do a bunch at once (note we could have also done this when we created the environment, but we are learning here!)
2. ```conda install scipy seaborn scikit-image fsspec hdf5 scikit-learn statsmodels numba pytables```

### We should be good for the couple of days of python fun in bootcamp. 
Of course, we can always add packages later as we need them, using a terminal and ```conda install name_of_my_package```or ```pip install name_of_my_package```

### One more thing - Github Desktop or VS Code or command line git management. 
We will start the later session with a short introduction to version/source contol with git, includig a walkthrough of how to use it to get the Introductory and independent content for the course. 


