# Prototype


Lets creation of new objects using copying of prototype object.

There three components needed for the prototype pattern are as follows:
- Client creates a new object by asking a prototype to clone itself;
- Prototype declares an interface for cloning yourself;
- Concrete prototype implements the operation for cloning itself;

Advantages:
- It delegates the cloning process to the actual objects that are being cloned. 
That's why it does not depend on concrete classes cloning logic;
- You can reduce the number of subclasses that only differ in the way they initialize (specific configuration)
their respective objects. For instance, school and university buildings can be expressed by `Building` class 
  only with different parameters, but not wih separate classes like `School` and `University`;