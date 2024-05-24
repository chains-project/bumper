```java
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TIOStreamTransport;

TTransport transport = new TIOStreamTransport(System.in, System.out);
```