Here is a patch that you can apply to the code:

```java
import org.apache. thrift.transport.TTransport;
import org.apache. thrift.transport.TFramedTransport;

TTransport transport = new TFramedTransport(new TTransport());
```

This patch imports the `TTransport` class from the `org.apache.thrift.transport` package, which is a dependency of `TFramedTransport`. The `TTransport` class is then used to create a new `TFramedTransport` object. This should fix the "cannot find symbol" error that you are seeing.