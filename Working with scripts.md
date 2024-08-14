## Scripts 
#### For bootcamp and in NSP courses we use VS Code to do some data exploration and analysis in a Jupyter notebook. 
This is a very efficient way to do data exploration, analysis, and figure making. But there are certainly cases where you want the computer to run something in the background, or execute one thing and be done. In these cases, you might opt for writing a python script, a ```.py``` file that you can invoke from the command line. 

#### It can also be very useful to make a script that runs from start to end without the chance to jump in and write code
1. One use of a script is a standalone analysis - press go (by running the script) and everything just goes until it is done.
2. Another is a process that runs on a timer in the background - start a script that runs forever, or runs on a timer, for automatically doing tasks. This useful for automatically backing up data or posting the results of experiments to Slack as they come in. 
3. Scripts are also good as the logical control for a behavioral task an animal is performing (i.e., interacting with the joystick). We are making a video game for science here. Other good uses of scripts in the lab are moving data around the network in an automated way; standalone scripts that regenerate a figure based on updated data (similar to the FluorescenceAnalysis Jupyter notebook we made yesterday). There are plenty more. While doing so, we will go over more flow control (loops, conditional statements) and object-oriented programming. 

We aren't covering scripts more in bootcamp. But the concept is straightforward. Any code you wrote in cell a notebook you could copy/paste into a file. If you save that file as `.py` your computer will know it is a python script. If you open a terminal (in VS code, on the bottom panel which you can see with Ctrl+J or ⌘+J) you then simply run `python name_of_your_script_file.py` from the folder where that file is saved on your computer. 

<br>
<br>
<br>
