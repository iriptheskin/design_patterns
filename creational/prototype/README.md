# Prototype

(Still unclear)

Lets creation of new objects using copying of prototype object.

There three components needed for the prototype pattern are as follows:
- Client creates a new object by asking a prototype to clone itself;
- Prototype declares an interface for cloning yourself;
- Concrete prototype implements the operation for cloning itself;

It delegates the cloning process to the actual objects that are being cloned. 
That's why it does not depend on concrete classes cloning logic.  