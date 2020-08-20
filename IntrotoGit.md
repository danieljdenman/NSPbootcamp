git is a form of version control. it helps manage versions of code - whether that is your own versions, or versions shared between people. it is typically invoked from the command line, but can also be used through the GitHub gui. 

git is powerful, but it can also be tricky and confusing to learn! here is a good resource for understaning how it works:<br>
[learn it visually](https://learngitbranching.js.org/)

we're going to use it to get the resources for class today. the ```git clone``` command will pull, from GitHub where they are hosted, materials like Jupyter notebooks and data into a folder on your computer. first, navigate using ```cd``` to a folder where you want to keep this data. i keep all of my git repositories (folders) in a folder called "github"; you could keep yours in such a folder, or on your desktop, or in Documents, etc. so from a terminal i will run: <br>
```cd /Users/danieljdenman/github```

after you do that, then run: <br>
```git clone https://github.com/danieljdenman/NSPbootcamp.git```

and in your folder you will find a new folder, called "NSPbootcamp"