# Singleton

There is possible to instantiate only one object of a class, during program execution.
 

Advantages:
- Use the Singleton pattern when you need stricter control over global variables;
- Use it when you need a single instance available for all clients, for instance logger;

The main criticism of the singleton pattern is that it's just a pretty way to get a global
state which is one of the things you want to avoid when writing programs. It's because one part of your program 
can alter the global state and cause unexpected results in another place.

No part of the program attempts to make a change in the singleton, and 
as such there is no danger of one part of the project interfering with another
part of the project because of the shared state.
