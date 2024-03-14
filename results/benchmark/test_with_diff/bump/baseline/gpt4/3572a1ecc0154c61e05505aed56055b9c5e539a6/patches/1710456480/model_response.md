```java
import org.apache.thrift.transport.TIOStreamTransport;
import org.apache.thrift.TConfiguration;
import java.io.InputStream;
import java.io.OutputStream;

// Replace TFastFramedTransport with TIOStreamTransport
TConfiguration tConfiguration = new TConfiguration();
InputStream inputStream;
OutputStream outputStream;

TIOStreamTransport tIOStreamTransport = new TIOStreamTransport(tConfiguration, inputStream, outputStream);
```