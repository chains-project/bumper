```java
import org.apache.thrift.transport.TIOStreamTransport;
import org.apache.thrift.TConfiguration;
import java.io.InputStream;
import java.io.OutputStream;

// replace TFastFramedTransport with TIOStreamTransport
TConfiguration config = new TConfiguration();
InputStream input = // your input stream here
OutputStream output = // your output stream here
TIOStreamTransport transport = new TIOStreamTransport(config, input, output);
```