Here's a patch that you can apply to the code:

```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TFramedTransport;

TTransport rawTransport = ... // Initialize your raw transport here
TFramedTransport framedTransport = new TFramedTransport(rawTransport);
```

Replace the failing line with the second line of the patch. The `TFramedTransport` constructor now expects a `TTransport` instance, so initialize your raw transport and pass it to the `TFramedTransport` constructor.