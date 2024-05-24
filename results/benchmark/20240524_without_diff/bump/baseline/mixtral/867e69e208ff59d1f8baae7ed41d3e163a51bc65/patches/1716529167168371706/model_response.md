Here is a possible patch for the failing code:

```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TNonblockingTransport;
import org.apache.thrift.transport.layered.TFramedTransport$Factory;

// ...

TFramedTransport transport = new TFramedTransport(new TNonblockingTransport(new TFramedTransport.Factory()));
```

This patch creates a new `TFramedTransport` using the `TFramedTransport$Factory` instead of the deprecated `TFramedTransport$Factory()` constructor. It also wraps the `TFramedTransport` in a `TNonblockingTransport` to satisfy the type of the `TFramedTransport` constructor.

Note that this patch assumes that the `TFramedTransport` constructor with a single `TTransport` argument is still available in the new library version. If it is not, you may need to modify the patch accordingly.