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
>  
> **git rm -f <file name>**:  To delete a file (force).
> 
> **git rm -r --cached <directory name>**: To remove an entire directory from the working index (cached).
> 
> **git rm -r -f <file name>**: To delete an entire directory (force).


> # difference betwenn https and ssh
>
> # ***HHTPS, The Pro***
> The simplicity of having a single URL for all types of access and having the server prompt only when authentication is needed makes things very 
>
> easy for the end user. Being able to authenticate with a username and password is also a big advantage over SSH, since users don’t have to generate
>
> SSH keys locally and upload their public key to the server before being able to interact with it. For less sophisticated users, or users on systems
> 
> where SSH is less common, this is a major advantage in usability. It is also a very fast and efficient protocol, similar to the SSH one.
>
> # ***HHTP, The Cons***
> Git over HTTPS can be a little more tricky to set up compared to SSH on some servers. Other than that, 
>
> there is very little advantage that other protocols have over Smart HTTP for serving Git content.
>
> If you’re using HTTP for authenticated pushing, providing your credentials is sometimes more complicated than using keys over SSH.
>
> # ***SSH, the Pro***
> The pros of using SSH are many. First, SSH is relatively easy to set up--SSH daemons are commonplace, many network admins have experience with
>
> them, and many OS distributions are set up with them or have tools to manage them. Next, access over SSH is secure--all data transfer is encrypted
>
> and authenticated. Last, like the HTTPS, Git and Local protocols, SSH is efficient, making the data as compact as possible before transferring it.
>
> # ***SSH, the Cons***
> The negative aspect of SSH is that it doesn’t support anonymous access to your Git repository. If you’re using SSH, people must have SSH access to
>
> your machine, even in a read-only capacity, which doesn’t make SSH conducive to open source projects for which people might simply want to clone
>
> your repository to examine it. If you’re using it only within your corporate network, SSH may be the only protocol you need to deal with. If you
>
> want to allow anonymous read-only access to your projects and also want to use SSH, you’ll have to set up SSH for you to push over but something
>
> else for others to fetch from.

 

