# git
git is a form of version control. it helps manage versions of code - whether that is your own versions, or versions shared between people. it is typically invoked from the command line, but can also be used through the GitHub gui. One way to think about version control: track changes for the whole codebase, backed up in the cloud. you can always rewind to a point before you broke things. at any given point you are going to track a "branch" of a git repository (codebase / folder)

git is powerful, but it can also be tricky and confusing to learn! here is a good resource for understaning how it works:<br>
[learn it visually](https://learngitbranching.js.org/). There are two primary ways to use git - from the command line, or from a graphical client. We recommend [Github Desktop](https://desktop.github.com/). Both ways require a github account. If you don't have one, sign up for one at [GitHub](https://github.com/) before downloading and using the client 

we're going to use it to get the resources for class today. 
## from Github Desktop
1. download [Github Desktop](https://desktop.github.com/)
  (you will need to make a github account; go ahead and do this with whatever email you want. a free acccount is great, no need for Pro or anything!)
2. use a browser to go to https://github.com/danieljdenman/NSPbootcamp/, click on the Big Green "Code" button, and copy the URL
3. from Github Desktop, go to File>Clone Repository...
4. from the URL tab, paste what you copied
5. choose a folder where you will keep this code
6. press clone!

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
