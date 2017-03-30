# Tournament-Results
Developed a database schema to store the game matches between players. And written code to query this data and determine the winners of various games.

Installation needed:
  - Virtual Box
  - Vagrant Machine  
> Guide for installation goes [here](https://www.google.com/url?q=https://www.udacity.com/wiki/ud197/install-vagrant&sa=D&ust=1490854878829000&usg=AFQjCNFHekjbFdZ6IjFikEkXl0kKS2jfXg).
- Next fork and clone the [fullstack-nanodegree-vm repo](https://www.google.com/url?q=http://github.com/udacity/fullstack-nanodegree-vm&sa=D&ust=1490854878831000&usg=AFQjCNFLyYQ_rt2ifBZCxIdJK3XN7CpLzg) to your local machine.
# Using the Vagrant Virtual Machine

  - The Vagrant VM has PostgreSQL installed and configured, as well as the psql command line interface (CLI), so that you don't have to install or configure them on your local machine.
  - To use the Vagrant virtual machine, navigate to the full-stack-nanodegree-vm/tournament directory in the terminal, then use the command vagrant up (powers on the virtual machine) followed by vagrant ssh (logs into the virtual machine).
  - Remember, once you have executed the vagrant ssh command, you will want to cd /vagrant to change directory in order to work on your project, once your cd /vagrant, if you type ls on the command line, you'll see your tournament folder.
  - The Vagrant VM provided in the fullstack repo already has PostgreSQL server installed, as well as the psql command line interface (CLI), so you'll need to have your VM on and be logged into it to run your database configuration file (tournament.sql), and test your Python file with tournament_test.py.

### Understand the purpose of each file:

- tournament.sql  - this file is used to set up your database schema (the table representation of your data structure).
- tournament.py - this file is used to provide access to your database via a library of functions which can add, delete or query data in your database to another python program (a client program). Remember that when you define a function, it does not execute, it simply means the function is defined to run a specific set of instructions when called.
- tournament_test.py - this is a client program which will use your functions written in the tournament.py module. We've written this client program to test your implementation of functions in tournament.py


### Running your project!
Once you have your .sql and .py files set up like I did in my repo, log into your VM and go to the synced folders by typing 
```sh 
cd /vagrant/tournament
```
then, run the series of tests defined in this test suite using the command line 
```sh
$ python tournament_test.py 
```
You should be able to see the output with all your tests have passed.
> If your tests don’t pass that’s okay! The test suite will print explanations of what didn’t work. You can read the tests themselves to see exactly how they work.

