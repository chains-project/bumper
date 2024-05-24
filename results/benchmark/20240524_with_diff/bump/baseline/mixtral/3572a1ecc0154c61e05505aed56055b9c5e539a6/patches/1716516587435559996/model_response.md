Here's a patch that you can apply to fix the error:

```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TTransport;

// ...

TFastFramedTransport transport = new TFramedTransport(new TTransport());
```

This code creates a `TFramedTransport` using the constructor `TFramedTransport(TTransport trans)`, which is available in the new library version. The `TFastFramedTransport` class has been removed, so we can't use it directly. Instead, we use the `TFramedTransport` class, which provides similar functionality. Note that we can't use the `TFastFramedTransport$Factory` class anymore, so we need to create the `TFramedTransport` object directly.