```java
import org.apache.thrift.transport.TIOStreamTransport;
import org.apache.thrift.TConfiguration;

TConfiguration tConfiguration = new TConfiguration();
TIOStreamTransport transport = new TIOStreamTransport(tConfiguration);
```