Here's a possible patch for the failing client code:

```java
import org.apache.thrift.transport.FramedTransport;

// ...

TFramedTransport transport = new FramedTransport(socket);
```

In the updated library version, the `TFramedTransport` class has been renamed to `FramedTransport`. Therefore, we need to import the new class name and adjust the instantiation accordingly.