Here is the patched code:

```java
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.TConfiguration;

TFramedTransport transport = new TFramedTransport(new TConfiguration(), underlyingTransport);
```