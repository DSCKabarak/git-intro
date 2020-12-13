### github

Helps you check on your different versions.

Keep track of changes made in a file

### Common Commands and meaning

    /*diff*/-->show the difference in two files

        diff file_name1.py file_name2.py

    /*diff -u**/--> shows more changes in details

        diff -u file_name1.py file_name2.py

        uses ++ for added lines and -- for removed files

    /*wdiff*/ --> words that have changed in a file

    /*meld,KDiff3,vimdiff*/ shows changes in a more graphic way


#### =======================================latetest commit

### Applying changes made to a file

### check the py files for the used scripts and variables in examples

    patch-->apply changes made to a file as either </>
    patch cpu_usage.py < cpu_usage.diff

### example: check for error fix in code for low space usage

    start by creating copies of each case
        cp disk_usage.py disk_usage_original.py
        cp disk_usage.py disk_usage_fixed.py
    after the fix,now commit the changes made to you college
        patch disk_usage.py  < disk_usage.diff

### Cheat Sheet

    diff
        diff is used to find differences between two files. On its own, it’s a bit hard to use; instead, use it with diff -u to find lines which differ in two files:

    diff -u
        diff -u is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output. See below:

            ~$ cat menu1.txt 
            Menu1:

            Apples
            Bananas
            Oranges
            Pears

            ~$ cat menu2.txt 
            Menu:

            Apples
            Bananas
            Grapes
            Strawberries

            ~$ diff -u menu1.txt menu2.txt 
            --- menu1.txt   2019-12-16 18:46:13.794879924 +0900
            +++ menu2.txt   2019-12-16 18:46:42.090995670 +0900
            @@ -1,6 +1,6 @@
            -Menu1:
            +Menu:

            Apples
            Bananas
            -Oranges
            -Pears
            +Grapes
            +Strawberries
    Patch
        Patch is useful for applying file differences. See the below example, which compares two files. The comparison is saved as a .diff file, which is then patched to the    original file!
            ~$ cat hello_world.txt 
            Hello World
            ~$ cat hello_world_long.txt 
            Hello World

            It's a wonderful day!
            ~$ diff -u hello_world.txt hello_world_long.txt 
            --- hello_world.txt     2019-12-16 19:24:12.556102821 +0900
            +++ hello_world_long.txt        2019-12-16 19:24:38.944207773 +0900
            @@ -1 +1,3 @@
            Hello World
            +
            +It's a wonderful day!
            ~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff
            ~$ patch < hello_world.diff 
            patching file hello_world.txt
            ~$ cat hello_world.txt 
            Hello World

            It's a wonderful day!


## Module Reference

[Patch and diff commands](http://man7.org/linux/man-pages/man1/diff.1.html)

[Patch more details](http://man7.org/linux/man-pages/man1/patch.1.html)


### Installing Git on Windows

check for the version with

        git --version

[Download page](https://git-scm.com/downloads)

[installation Instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Working with Git.

Configuration:

    we user the flag - to set to all repositories
    
    git config --global user.email "timzowen@gmail.com"
    
    git config --global user.name "Timz Owen"

### create using simple project

    mkdir gitChecks-------> creates a new file on your system
    
    cd into the project file
    
    git init----->creates a new repository
    
    ls -la --->checks if file exits, list all starting with .
    
    ls -l .git --->check the contents in the file

    #staging area (File maintained by Git containing all the files and changes to the next commit)
    
    git add filename.py------->keep track of all file changes (staging area)
    
    git status------> check the current working tree and pending changes made
    
    git commit----->committing the changes made (you can write a commit message)

### Tracking File changes

