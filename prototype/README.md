# Prototype

In the prototype pattern, we favor composition over inheritance.

There three components needed for the prototype pattern are as follows:
- Client creates a new object by asking a prototype tp clone itself;
- Prototype declares an interface for cloning yourself;
- Concrete prototype implements the operation for cloning itself;

Classes that are composed of parts allow you to substitute those parts at runtime, profoundly
affecting the testability and maintainability of the system. The classes to instantiate are specified at runtime
by means of dynamic loading. The result of this characteristic of the prototype patter is that sub-classing 
is reduced significantly. The complexities of creating a new instance are hidden from client. All of this
is great, but the main benefit of this pattern is that ift forces you to program to an interface,
which leads to better design.

