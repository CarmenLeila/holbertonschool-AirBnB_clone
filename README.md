![](https://i.imgur.com/GM1iQ0P.png)

# <h1 align="center"> HolbertonBnB </h1>
# <p align="center"> An AirBnB clone </p>
This project is to provide hands-on experience in building a full web application, including backend logic, data modeling, command-line interfaces, and possibly front-end components. It also helps in understanding concepts like HTML/CSS templating, database storage, API, front-end integration…

![](https://i.imgur.com/dtPVtVd.png)

## 🛠️ Console
1. Clone this git repository

```bash
git clone https://github.com/CarmenLeila/holbertonschool-AirBnB_clone.git
cd holbertonschool-AirBnB_clone
```
2. You can now use the command interpreter

```bash
./console
```
3. If all is good, the following prompt should appear

```bash
(hbtn)
```


# Learning Objectives
## General
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
# Requirements
## Python Scripts
* Allowed editors: vi , vim , emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3(version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
# Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
* e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Classes:
HolbertonBnB utilizes the following classes:

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |
# Execution
HBNB should work like this in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF help  quit
(hbnb) 
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```
## Testing :straight_ruler:

Unittests for the HolbertonBnB project are defined in the [tests](./tests) 
folder.All tests should pass in non-interactive mode:

```
$ echo "python3 unittest -m discover tests" | bash 
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors :black_nib:
* **Carmen Leila MUGISHA** <[CarmenLeila](https://github.com/CarmenLeila)>
* **Nathan Vertueux** <[Nathan9722](https://github.com/Nathan9722)>
