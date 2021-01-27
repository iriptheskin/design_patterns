# Singleton

There is possible to instantiate only one object of a class, during program execution.

When you have parts of a project that don't affect the execution of your code, like logging,
it's acceptable to use global state. (as well as caching, load balancing, route mapping)


The main criticism of the singleton pattern is that it's just a pretty way to get a global
state which is one of the things you want to avoid when writing programs. It's because one part of your program 
can alter the global state and cause unexpected results in another place.

No part of the program attempts to make a change in the singleton, and 
as such there is no danger of one part of the project interfering with another
part of the project because of the shared state.
