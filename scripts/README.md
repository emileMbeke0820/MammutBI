
 # Here’s a Quick Way to Learn About Installing Packages using PIP in Python 
   It is impossible to write or develop a Python application without using the mysterious pip install command.
   
## What is PIP and why its matters?

>  Pip stands for Python Install Packages or Python Packages Manager. 
>  When you install python on your system, it comes with a set of pre-defined packages that are present in the Python standard library. 
>  Examples include DateTime, string, math, etc.
>  To install packages not including in the standard python libraries, Developer use the command pip install <package-name>
>  which install additional packages by default from the [PyPi](https://packaging.python.org/en/latest/tutorials/installing-packages/)
 

> # What PiP Install ?
> This commands have several advantages. Here are some:
> **Identify the base requirements.**: It processes User-supplied arguments.
> **Resolve dependencies.**: It determines which dependencies can/should be. 
> **Build wheels.**: All necessary dependencies are built here.
> **Install the packages**: and uninstall anything being upgraded/replaced

> # Commonly used Commands
 
 * pip --version:check the version of the pip installed which confirms you have pip installed. Otherwise, you should install PiP first.
 * pip --help/-h: This command will list down all the options and commands that you can use in pip. 
 * pip search: For any package, this command returns details like name, version, summary, dependent packages and much more.
 > # Example: pip show faker
	 
	> Name: Faker
	> Version: 4.1.8
	> Summary: Faker is a Python package that generates fake data for you.
	> Home-page: https://github.com/joke2k/faker
	> Author: joke2k
	> Author-email: joke2k@gmail.com
	> License: MIT License
	> Location: c:\users\eessammb\pycharmprojects\mammuttest\venv\lib\site-packages
	> Requires: python-dateutil, text-unidecode
	> Required-by: db-faker

 
 * pip list: The pip list command returns the list of packages in the current environment. It also returns the installed version for each package.
 * pip freeze: to freeze the packages and their current version. pip freeze is most useful when we want to use the same set of packages 
   on different platforms or environments. ( pip freeze > filename.txt)
 
 * pip install -r <filenmae>: We use this command to set up another environment or if we share our code, they have an idea 
   of the packages needed to run our code.



># Requirement Files
>  Requirements files serve as a list of items to be installed by pip, when using pip install.
>  The command pip install -r requirements.txt install from the given requirements file.
>  The -r is a global supported options by pip install. They have an effect on the entire pip install run and must be
>  specified on their individual lines. 
> # another options and their meaning:
	> -e, --editable <path/url>: Install a project in editable mode. 
	> -U, --upgrade: Upgrade all specified packages to the newest available version. 
	> -c, --constraint <file>: Constraints files are used for exactly the same reason as requirements files 
	> when you don’t know exactly what things you want to install.
	

# BI Folder Struktur 
> A good BI should constains 
> A Databases Folder for all your databases operations (DDL;DML; and so on and so forth)
> A Scripts Folder for your code/script . e.g: python or Java Scripts.
> A Log packages for releasing log messages occured when the software are running. 
> A Output Folder for analysing the logs messages deeper.
> An Install Folder for installed packages or required packages. This can be helpful when you come back to your code later. 















































	

	