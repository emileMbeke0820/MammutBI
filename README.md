
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

 

