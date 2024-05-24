Here's a patch that you can apply to fix the error:

```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TNonblockingTransport;
import org.apache.thrift.transport.layered.TFramedTransport$Factory;

// ...

TNonblockingTransport rawTransport = new TNonblockingTransport(new TConfiguration());
TFramedTransport transport = new TFramedTransport.Factory().createTransport(rawTransport);
```

This code creates a new `TNonblockingTransport` using the `TConfiguration` constructor that was added in the new library version. Then, it creates a new `TFramedTransport` using the `TFramedTransport$Factory` that was added in the new library version. The `createTransport` method is used to initialize the `TFramedTransport` with the `TNonblockingTransport`.