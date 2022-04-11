# Repo für den Einsatz bei Mammut



> # Substask 1, Some basics Git commands.
>
> **git clone [url]**: Clone a repository from a remote.
> 
> **git status**: Check the status of a git repository.
> 
> **git add [filename]**: Stage a particular file for commit.
> 
> **git add .**: Stage all changes in the current directory for commit.
> 
> **git commit -m "Your message here"**: Commit the staged changes. 
> 
> **git push**: Push local commits to a remote repository.
> 
> **git push -u [remote name] [remote branch (master)]**: Push local commits to a remote.
> 
> repository, saving the specifics of where that code should end up.
> 
> **git pull**: Retrieve the latest changes from a remote (teams, multiple computers).
> 
> **git init**: Create a new git repository in the current working directory.
> 
> **git config --global user.name "Your Name Here"**: Set the name to include in all future commits (initial setup).
> 
> **git config --global user.email "yourEmailHere@something.com"**: Set the email address to include in all future commits (initial setup).
> 
> **git branch <branch_name>**:  Create a new branch.
> 
> **git branch -a/--list**:  List all remote or local branches.
>
> **git branch -d <branch_name>**: Delete a branch.
> 
> **git rm --cached <file name>**: To remove a file from the working index (cached).
  
> **git rm -f <file name>**:  To delete a file (force).
  
> **git rm -r --cached <directory name>**: To remove an entire directory from the working index (cached).
  
> **git rm -r -f <file name>**: To delete an entire directory (force).


# > difference betwenn https and ssh
 

> Https and SSH are two protocols used to identify yourself. There is not such a big diference between them. The main difference is that
>
>  https is less complicated and faster than ssh. But everytime you use it, you'll be asking to enter your username and passowrd, which .
>
> isn't always fun. SSH on the other hand is hard to configure but more secure and once you generate your ssh key pair and add it to your 
>
> GitHub account, GitHub will reconize it everytime you connect. If however you want to keep it with https without entering your username  
>
> and password each time, you should create a Credential Helper Manage with the command :  git config --global credential.helper cache . 
>
> Git will generate a personnal access token for you and there will be no need to enter your 

> username and passowrd again. 