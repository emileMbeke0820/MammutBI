### Repo für den Einsatz bei Mammut





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



> ### difference betwenn https and ssh

 
> ### HTTPS
> It uses password authentication for pushing. 
> You will be asking to enter your GitHub passowrd every time you push. It's possible for Git to remember your password for a few minute.
> It is been said that HTTPS is less secure than SSH because you have to store your GitHub Account permanently, which is very risky and 
> can be hacked. 
> To avoid using your password everytime you push, you have to enebale two-factor authentication and use personal access token.

> ### personal access token
> Personal access tokens (PATs) are an alternative to using passwords for authentication to GitHub when using the GitHub API or the command line.
> 1. The first step is to verify your email if not verified yet.
> 2. Click your profile photo then Settings
> 3. In the left sidebar, click  Developer settings then click Personal access tokens.
> 4. Click Generate new token and give it a name of your choice.
> 5. Select the Expiration drop-down menu, then click a default or use the calendar picker to give your token an expiration. 
> PS: As a security precaution, GitHub automatically removes personal access tokens that haven't been used in a year. 
> 6. To use your token to access repositories from the command line, select repo. You can also select the scopes, or permissions, you'd like to grant >    this token.
> 7. Click Generate token , GitHub will confirm it. That's all. 
> According to GitHub-documentation, HTTPS is in some cases a little faster than SSH, especially over high-latency connections.
> Git Credential Manager (GCM) is another way to store your credentials securely and connect to GitHub over HTTPS. With GCM, you don't have to 
> manually create and store a PAT, as GCM manages authentication on your behalf, including 2FA (two-factor authentication).




> ### SSH
> To use public-key authentication, You have to generate a keypair (or "public key"), then add it to your GitHub account.
> Using keys is more secure than passwords, since you can add many to the same account 
>(for example, a key for every computer you use GitHub from). The private keys on your computer can be protected with passphrases
> GitHub does not require two-factor auth since we don't use a password for ssh.
> With the public-key, you can push and pull but not edit your GitHub, which is good in case you lose your private key. All you have to do is 
> to remove is from your Account. 
> You can follow 
> [this link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
> to generate a ssk-key.
