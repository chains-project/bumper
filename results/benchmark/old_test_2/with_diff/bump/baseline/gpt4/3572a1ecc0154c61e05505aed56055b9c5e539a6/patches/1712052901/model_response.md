```java
import org.apache.thrift.transport.TIOStreamTransport;
import org.apache.thrift.TConfiguration;

TConfiguration tConfiguration = new TConfiguration();
TIOStreamTransport tIOStreamTransport = new TIOStreamTransport(tConfiguration);
```