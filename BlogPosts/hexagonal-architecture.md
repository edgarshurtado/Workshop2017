# [Hexagonal Architecture](http://fideloper.com/hexagonal-architecture)

> Hexagonal Architecture is NOT a new way to think about programming within a framework. Instead, if's a way of describing "best practices" - practices that are both old and new

> The article takes on a shape of a hexagon. The number of sides is actually arbitrary. The point is that is has many sides. Each side represents a "port" into or out of our application.

> A port can be thought of as a vector for accepting requests (or data) into an application. For example, an HTTP port (browser requests, API) can make requests on our application. Similarly, a queue worker or other messaging protocol (perhaps AMQP) can also make a request on our application. These are different ports into our application, but are also part of the "request port". Other ports could include those for data access, such as a database port.

The objective of the architecture:
1. High maintainability
2. Low Technical Debt

The author states that this 2 concepts are the same. Maintainability reduces the rate of increasement of technical debt. Hence, to do changes is easier.

Measures of a highly maintainable application:

1. Changes in one area of an application should affect as few other places as possible
2. Adding features should not require large code-base changes
3. Adding new ways to interact with the application should require as few changes as possible
4. Debugging should require as few work-arounds and "just this once" hacks as possible
5. Testing should be relatively easy

For making an application maintainable we **Identify the aspects that vary and separate them from what stays the same**

Paterns shown in the article to increase maintainability:
* Interfaces
* Decorators

> Creating interfaces for portions of our application that may change is a way to encapsulate change. We can create a new implementations or add more features around an existing implementation as needed with strategic use of interfaces.

## Layers

> Hexagonal Architecture, a layered architecture, is also called the Ports and Adapters architecture. This is because it has the concept of different ports, which can be adapted for any given layer.


Each layer has two elements:
1. The Code (here we find the adapters (implementations), and other business logic)
2. The Boundary (here we find the ports (interfaces) that define how outside layers can communicate to the current layer)

### Domain Layer

Contains the business logic and defines hot the layer outside of it can interact with it.

In this layer we encounter behaviours and constraints of our aplications. Besides this Core Domain, we find also supporting domain logic such as Domain Events and use-cases(definitions of what actions can be taken on our applications)

### Application Layer

Handles the entities fount ins the Domain Layer . It's also the glue between the domain layer and the application layer.

### Framework Layer

Contains code that your application uses but it is not actually your application.

Alaso adapts requests from the outside to our Application Layer (like user input and http requests)

## Comunication between layers

Each layer is responsible for the comunication with the next outside layer. This is done through interfaces.

The interface is the port, and the implementation is de adapter of the port

So each layer will define an interface on how it will use the outter layer

## Vocabulary
* succintly: brevemente
* blatantly: abiertamente/descaradamente
