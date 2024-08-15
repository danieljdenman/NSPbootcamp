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