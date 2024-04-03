Here's a patch that should fix the error:

```java
import org.apache.thrift.transport.FramedTransport;

// ...

TFramedTransport transport = new FramedTransport(socket);
```

This patch replaces the import statement with the new name of the FramedTransport class. It also creates a new FramedTransport object with the same parameters as before. Note that the FramedTransport class has the same functionality as the TFramedTransport class, but with a different name.