# Installation

We will install a package management system, a code editor, and version control system. (For reference, as of 2023 installing MATLAB includes each of these, but with Python we do this separately.) 
- A package management system, which helps us [install packages and create and maintain separate environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) for separate programming tasks. We will now install Anaconda, to do this. One of the great things about python is that we can leverage all of that public and free code out there. Great! One disadvantage: not everyone in the world has coordinated their code bases to work with everyone else's 🤼‍♂️ 🖥 🤺 . this means that Jane's very_useful_package may require a numpy version that conflicts with Bob's pretty_good_tool. The solution: create seprate environments for working with Jane's very_useful_package and Bob's pretty_good_tool. For science, examples might include separate environments for image analysis, Arduino control, for data analysis of RNAseq data, for analysis of Ca2+ imaging data....or even a course (like this one) or a home project scraping data from instagram.
- A code editor makes it a little prettier to write code and see outputs than it might be writing code in a blank unformatted document (which is also an option...)
- A version control system helps you get and share code with others. What's not to love, using code that other people wrote?

## A. Install Anaconda for package and environment management
[Download](https://www.anaconda.com/products/individual) and [install](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) Anaconda.

## B. Install a code editor. 
Choosing an editor is a personal choice that can generate strong opinions. [There are many options](https://hackr.io/blog/best-python-ide). If you don't already have a strong preference, we'll use a fully featured and very popular one: VS Code. [Download and install VS Code](https://code.visualstudio.com/). If you do already have a strong preference, great! That means you know how to use it, but please be confirm you know how to use your editor with a git workflow, as this will be used to manage code work for the first year NSP courses. 

## C.1 Install git. 
Download and install git in your system using the official [website](https://git-scm.com/downloads). If you think you might already have git, open a terminal (in VS Code press press Ctrl+J or ⌘+J) and confirm with 
```
git -version
```

# For 2025 NSP bootcamp, stop here 🛑 

## C.2 Create a Github account and link it to VS Code.
1. Go to [Github](https://www.github.com) and create an account. You can use any email you want including your anschutz.edu or a personal email. 
2. Configure VS Code to use your Github account. Open a VS code Terminal (press Ctrl+J or ⌘+J) and enter the below, one line at a time, replacing the "Your..." with your information. 
```
git config –global user.name “YourUserNameOnGithub”
```
```
git config –global user.email “YourEmail”
```
