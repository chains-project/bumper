```java
import org.apache.thrift.TConfiguration;
import org.apache.thrift.transport.TIOStreamTransport;
import java.io.InputStream;
import java.io.OutputStream;

TConfiguration tConfiguration = new TConfiguration();
InputStream inputStream = // initialize it as per your requirement
OutputStream outputStream = // initialize it as per your requirement

TIOStreamTransport tIOStreamTransport = new TIOStreamTransport(tConfiguration, inputStream, outputStream);
```