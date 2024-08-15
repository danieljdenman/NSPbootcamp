# git
git is a form of version control. it helps manage versions of code - whether that is your own versions, or versions shared between people. it is typically invoked from the command line, but can also be used through a graphical interface (Github Desktop or VS Code). One way to think about version control: track changes for the whole codebase, backed up in the cloud. you can always rewind to a point before you broke things. at any given point you are going to track a "branch" of a git repository (codebase / folder)

git is powerful, but it can also be tricky and confusing to learn! here is a good resource for understaning how it works:<br>
[learn it visually](https://learngitbranching.js.org/). There are two primary ways to use git - from the command line, or from a graphical client. For the first year of NSP, (bootcamp and some exercise in Intro to Neurosciennce and Systems Neuro) we recommend [VS Code]([https://desktop.github.com/](https://code.visualstudio.com/)). Both ways require a Github account. If you don't have one, sign up for one at [GitHub](https://github.com/). 

we're going to use _git_ to **get** the resources for class today. 
## from VS Code
1. use a browser to go to https://github.com/danieljdenman/NSPbootcamp/, click on the Big Green "Code" button, and copy the URL in the **HTTPS** section. 
3. on the left of VS code, click the Source Control icon. It looks like this:  ![icon](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftaiwrash.github.io%2Fg4-workshop%2Fbeginner-intermediate%2Fvscode-pack%2Fvscode-2.PNG&f=1&nofb=1&ipt=a1354472b8b3e0e795ae3c1c83015c767f0b9d59f6ee70d8b7eb80e78b4d413b&ipo=images)
4. from here, click the big blue _Clone Repository_ button.
5. in the top bar, choose either _Clone from URL_ or _Clone from Github_ and past the URL you copied above
6. from the system dialog choose the folder where you will keep this content. it can be anywhere; we'd recommend making a _Github_ folder within a sensible location like _Documents_ or _Desktop_
7. press OK!
8. after it is done, you can _Open this repository_. If you come back later, you can open a new VS code window (Shift+Ctrl+N or Shift+⌘+N), go to the Source Control tab, select _Open Folder_, and then navigate to wherever you selected for #6 above. 

## from the command line
the ```git clone``` command will pull, from GitHub where they are hosted, materials like Jupyter notebooks and data into a folder on your computer. first, navigate using ```cd``` to a folder where you want to keep this data. i keep all of my git repositories (folders) in a folder called "github"; you could keep yours in such a folder, or on your desktop, or in Documents, etc. so from a terminal i will run: <br>
```cd /Users/danieljdenman/github```

after you do that, then run: <br>
```git clone https://github.com/danieljdenman/NSPbootcamp.git```

and in your folder you will find a new folder, called "NSPbootcamp"

### some basic concepts:
#### ```git add```
you made a change to a file and you want to track that change. great! use ```git add name_of_file.extension``` to add it to the list of local files that git is ready to keep track of. 

#### ```git commit```
you're done making changes to your file, and you want to commit those changes to the record. great! use ```git commit -m "a description of what has changed"``` to record all of the files you have ```git add```ed 

#### ```git push```
after you have ```git add```ed and ```git commit```ed, use ```git push``` to actually "push" those changes to cloud

#### ```git pull```
somoeone else has been working on your branch? go team! use ```git pull``` to grab their changes from the cloud and put them on your computer. have you been also modifying things without pushing? conflict! you'll have to stash or merge. google these to figure out what to do. 
