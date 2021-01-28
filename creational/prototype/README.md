# Prototype


Lets creation of new objects using copying of prototype object.

There three components needed for the prototype pattern are as follows:
- Client creates a new object by asking a prototype to clone itself;
- Prototype declares an interface for cloning yourself;
- Concrete prototype implements the operation for cloning itself;

It delegates the cloning process to the actual objects that are being cloned. 
That's why it does not depend on concrete classes cloning logic.  

(Still unclear)
The classes to instantiate are specified at runtime by means of dynamic loading. 
The result of this characteristic of the prototype pattern is that sub-classing is reduced significantly.
Why?

Answer: For example, you have 1 base class and 2 concrete for an animal: Animal, Dog and Cat.

If your class Animal is descriptive enough, you can describe Dog and Cat
as Animal without using sub-classing but parametrizing of Animal class.
It reduces the number of sub-classes.