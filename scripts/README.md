
 # Here’s a Quick Way to Learn About Installing Packages using PIP in Python by Jessica Saini(medium.com)
 Either you are a newbie Python developer or an experienced one, it is impossible to write or develop a Python application without using the pip install command.
 # What is PIP?
>  Pip stands for Python Package Manager. 
   When you install python on your system, it comes with a set of pre-defined packages that are present in the Python standard library. Examples include DateTime, string, math, etc.
   PIP is a collection of software tools that automates the process of installing, upgrading, configuring, and removing computer programs for a computer’s operating system in a consistent manner. It allows you to install and manage additional packages that are not present in the Python standard library.
   If you want to install a package without pip, you need to perform the following steps:
   Download the package
   Unzip it if it is zipped
   Go to the directory using cd containing setup.py
   Type in python setup.py install
   If everything goes right, which rarely does in one go, the files will be installed into subdirectories of the site- USER_BASE.
   Now imagine, not doing any of the steps and just typing 3 words to get your installation done. Doesn’t that sound magical?
   Well, pip accomplishes it using the one-line command:
   pip install <library name>
   
 # Fundamentals of PIP
 Pip has become an integral part of Python. It is now included with the Python installer since versions 3.4 for Python 3 and 2.7.9 for Python 2.
 You can verify that pip is available by running the following command in your console:
 
 # Commonly used Commands
 * pip version:You can check the version of the pip installed in your system using the pip --version command.
 * pip help: This command will list down all the options and commands that you can use in pip. In order information about a specific command, use 	  pip help <command>
 * pip search:If you are looking for a package you can use the command pip search <query>. This command will search the packages available in PyPI  whose name or summary contains the words that you mentioned in the search query.
 
> # $ pip search data manipulation
> The above command will return the list of all the libraries whose name or summary contains the word “data manipulation”.

* pip list: You can see the list of installed versions using the pip list This command returns the list of packages along with the installed version in the current environment.

* pip list: You can see the list of installed versions using the pip list This command returns the list of packages along with the installed version in the current environment.

* Outdated packages: In case you want to check which packages are obsolete, use the pip list -o or pip list --outdatedcommand.

* Install the latest version of a package: Once you have identified the outdated packages using the pip list -o command, use the following command to install the latest version of the package. -U flag stands for update.
> # $ pip install -U <package-name> 

# Requirement Files

  When developing a piece of software in Python, it is customary to install a number of packages. You would have used pip install <package name> to install them in your local environment.
  Now imagine cloning your environment to another system. It will become extremely hard to run pip install for each of the packages and ensuring that we install the right version.
  To facilitate and make this process easier, pip allows you to create a requirements file. Requirements file gives you a way to create an environment: a set of packages that work together. It is basically a list of packages along with the corresponding version that you need to install in order to create your environment.
  If you want to see the list of packages with the version number, use the pip freeze command.
  What is Freeze?
  Freezing is a process where pip reads the versions of all installed packages in a local environment and then produces a text file with the package version for each python package specified. By convention, it’s named “requirements. txt ”.
  //This command will output the installed packages in the requirements format.
  $ pip freeze
  //This command will create a requirements.txt file with the list of installed packages and their corresponding versions.
  $ pip freeze > requirements.txt
  In order to install the dependencies using the requirements file, use the following command:
> $ pip install -r <name of the file requirement file>
> The -r flag indicates that there is a requirements file that pip needs to refer to

# Installing and Uninstalling Packages using Pip
  There are primarily 4 stages of installation using pip
  
 * Base Requirement Identification: The arguments or flags that are supplied in the command are processed. Pip checks which type of item each word in the command is.
 * Resolve dependencies: Find the version that pip needs to install.
 * Build wheels: A wheel is a ZIP-format archive with a specially formatted filename and the .whl extension. It is designed to contain all the filesfor a PEP 376 compatible install in a way that is very close to the on-disk format. All the dependencies with .whl extension are built.
 * Install the packages: Pip installs the dependencies( packages) before their dependents, i.e. in “topological order”. This is to avoid circular dependency and ensure that the concurrent environment is more likely to work.
 
 By default, all the packages that you install using the pip install command will be available in the site-packages directory.

# Different ways to Install Packages using PIP
	Pip allows you to install packages from the following sources:
	PyPI and other indexes
	Local project directories
	Local or remote source archives
	VCS project URLs.
	You can install a package using the pip install <package> command. By default, a package is installed from PyPI. Similarly, for uninstalling you need to use pip uninstall <package> .
	However, if you want to use a different index, you can use the —-index-url or -i flag in the command.
	$ pip install --index-url <url link>
	If you want to search an additional index use, the following command
	$ pip install --extra-index-url <url link>
	
#	Installation from Local Project Directories

	In order to install from a particular directory, you need to use the —- find-links flag along with the location of the directory containing the archives. In case, you do not want pip to search the PyPI, use the —- no-index flag.
	$ pip install --no-index --find-links=<location of the directory containing archives>
	
#	Installation from Remote or Source Archives

	If you have the dependencies available in your remote or source archives, you can directly use the pip installcommand to install them in your local environment.
	$ pip install <location of .gz, .zip file>
	
#	Installation from VCS

	In order to install from any Version Control System (VCS), you need to prefix the name along with the URL in the command. You also need to use the —e flag to install it in editable mode.
	$ pip install -e <vcs_name>+<url_link>
	So this brings us to the end of the post. I hope that after reading this blog post, you will be confident in understanding and using PIP.
	Happy Developing.
	
	Source: https://medium.com/swlh/heres-a-quick-way-to-learn-about-pip-in-python-18617d466c59
	
	 If you are looking fpr any python libraries and their role:
     Link: https://pythonmana.com/2021/09/20210907120415620U.html 