# Creating a Python module
An important step towards creating reusable code is to package its component functions
into a module that can be called from the Python path by any script. To start, we need to
create a folder as a sibling to your project or in the `site-packages` folder, where most Python modules are placed when
downloaded and extracted using the Python module process or using pip. Open up the
`site-packages` folder in Windows Explorer by navigating to the
`C:\Python27\ArcGIS10.5\Lib\site-packages` folder.

If you create your own functions to reuse those functions that you find useful, or to share
with other users, package the functions together as a module. Modules package together
functions in one or more scripts into a folder, which can be shared with others (though they
often depend on other modules to run). We have used some of the built-in modules, such as
the CSV module, and third-party modules, such as ArcPy. Let's explore their construction
to get a feel of how a module is packaged for use and sharing. Open the Chapter13 scripts
folder, and look in the functions folder. There is a special file inside the folder, which
allows the code inside the folder to be imported as a module, just like CSV or any other
Python module.

## The __init__.py file
Within the module folder (in this case, the folder functions), a special file has been added
to let Python recognize the folder as a module. This file, called __init__.py, takes
advantage of the special property of Python called “magic” objects or attributes, which are
built into Python. These “magic” objects use the leading and trailing double underscores to
avoid any confusion with custom functions.

These are double underscores. The single underscores are usually used for
so-called private functions within custom Python classes.
The __init__.py file is used to indicate that the folder is a module, which makes it
importable using the import keyword. The file can hold Python commands such as import
statements that initiate the module by calling any modules that it may rely on. However,
there is no requirement to add import commands to the __init__.py file; it can be an
empty file, and will still perform the module recognition functionality that we require as
follows:
1. Create a folder called common in the Lib\site-packages folder in your
Python27 installation (for example, C:\Python27\ArcGIS10.5\Lib\sitepackages).
1. Open up IDLE or your favorite IDE, and in the folder called common, add a new
Python file and call it __init__.py. This file will remain empty for now.
1. Now that we have initiated the module, we need to create a script that will hold
our common functions. Let's call it useful.py, because these functions will be
the most useful for this analysis and others. Save it into the common folder.
1. The next step is to transfer functions that we created in earlier chapters. These
valuable functions are locked into those scripts, so by adding them to
useful.py, we will make them available to all other scripts that we craft. Add
the createCSV and createXLS functions from Chapter 2, Creating the First
Python Script, useful.py, and any other functions that you have written and rely
on.
1. Now that the simple module is organized, the functions can be imported into a
script as follows:
 `from common.useful import createCSV, createXLS`
 
