```java
import org.apache.thrift.transport.TIOStreamTransport;
import org.apache.thrift.TConfiguration;
import java.io.InputStream;
import java.io.OutputStream;

TConfiguration tConfiguration = new TConfiguration();
InputStream inputStream = ...; // initialized somewhere
OutputStream outputStream = ...; // initialized somewhere

TIOStreamTransport tIOStreamTransport = new TIOStreamTransport(tConfiguration, inputStream, outputStream);
```