# QueueAndStacks
Manipulating Queues, Stacks, and Linked Lists through Classes and Methods only

# Project 5: Implementing ADTs

In this assignment we are implementing the ADTs we've been studying 
so far this semester: Linked Lists, Stacks, & Queues. We **will not** be
using _any_ built-in functions other than `range` or `len` and the `Node`
class provided.

Please complete implementing all 5 classes (**_Hint:_** we went over
3 of them in class). The constructors, fields, & method stubs are
started for you.

You can test the code by running the `pytest` or `python3` commands:

* To run just the main code for one problem: `python3 LinkedList.py`
* To run the tests for one problem: `pytest LinkedList_test.py`
* To run all the tests prior to submission: `pytest`

**NOTE: DO NOT run pytest until your main is working**
-- it may not stop running!

### Files that should (& shouldn't!) be changed

You **SHOULD** implement your problem solutions in the following files:
* `LinkedList.py`
* `StackLL.py`
* `QueueLL.py`
* `StackArray.py`
* `QueueArray.py`

You **SHOULD NOT** modify the following files:
* `Node.py`
* any constructors (i.e., `__init__` functions)

### Professionalism
In addition to passing the test cases and meeting the specifications / requirements (e.g., only using permitted built-in functions), your code will be assessed in terms of its **_professionalism_**:
* Following naming convetions: meaningful variable names beginning with a lower case letter, class names beginning with an upper case letter
* DRYness: avoiding unnecessary steps or copy & pasting code (use loops & functions instead!)
* Comments: adding comments to explain what lines in longer methods/functions are doing

## Problem 1: Linked List
Given a linked list defined by a `head Node`, please implement the following methods:
* `add(data)`: inserts a new `Node` with `data` into the front of the list
* `get_head()`: returns the data in the head node, and `None` otherwise
* `search(data)`: returns `True` if `data` is in the list, or `False` otherwise
* `delete(data)`: searches for `data` in the list, removes it if found and returns it, otherwise returns `None` and makes no change to the list
* `is_empty()`: returns `True` if the list is empty, or `False` otherwise
* `clear():` makes the list empty

## Problem 2: Stack-LL
Given a stack defined by a `top Node`, please implement the following methods:
* `push(data)`: adds a new `Node` with `data` on the top of the stack
* `peek()`: returns the data on the top of the stack, and `None` otherwise
* `pop()`: returns the data on the top of the stack, otherwise returns `None` if the stack is empty
* `is_empty()`: returns `True` if the stack is empty, or `False` otherwise
* `clear():` makes the stack empty

## Problem 3: Queue-LL
Given a queue defined by a `front` and `tail Node`, please implement the following methods:
* `enq(data)`: adds a new `Node` with `data` to the tail of the queue
* `deq()`: returns the data on the front of the queue and removes it, otherwise returns `None` if the queue is empty
* `get_front()`: returns the data at the front of the queue, and `None` otherwise
* `get_tail()`: returns the data at the tail of the queue, and `None` otherwise
* `is_empty()`: returns `True` if the queue is empty, or `False` otherwise
* `clear():` makes the queue empty

## Problem 4: Stack-Array
Given a stack defined by a `top` index and an `array`, please implement the following methods:
* `push(data)`: puts `data` on the top of the stack
* `peek()`: returns the data on the top of the stack, and `None` otherwise
* `pop()`: returns the data on the top of the stack, otherwise returns `None` if the stack is empty
* `is_empty()`: returns `True` if the stack is empty, or `False` otherwise
* `clear():` makes the stack empty

## Problem 5: Queue-Array
Given a queue defined by a `front` and `tail` index and an `array`, please implement the following methods:
* `enq(data)`: puts `data` on the tail of the queue
* `deq()`: returns the data on the front of the queue and removes it, otherwise returns `None` if the queue is empty
* `get_front()`: returns the data at the front of the queue, and `None` otherwise
* `get_tail()`: returns the data at the tail of the queue, and `None` otherwise
* `is_empty()`: returns `True` if the queue is empty, or `False` otherwise
* `clear():` makes the queue empty

## Getting started

### Develop online

Click the "Work in Repl.it" button. Edit the file. To run, see the commands below.

### Develop in PyCharm

With this option, you can develop on your laptop. 
You will need to install PyCharm (or another IDE),
git, and pytest. PyCharm has some built-in git 
support.

## Testing
Many of the tests are failing right now because the 
functions
aren't outputting the correct information. Fixing this
will make the tests pass & turn green.

### Setup
To use pytest on repl.it, install it first:

`pip3 install pytest`

To install pytest on the command line for running on a laptop (using a linux or unix based command-line like MacOS):

`sudo -H pip3 install pytest`

If using PyCharm, you may need to fix your project setup.
- Open the **Settings/Preferences | Tools | Python Integrated Tools** settings dialog.
- In the Default test runner field select **pytest**.
- Click OK to save the settings.

### Run commands
To run just the main code for one problem:

`python3 file.py`

To run the tests for one problem:

`pytest file_test.py`

To run all the tests prior to submission:

`pytest`

