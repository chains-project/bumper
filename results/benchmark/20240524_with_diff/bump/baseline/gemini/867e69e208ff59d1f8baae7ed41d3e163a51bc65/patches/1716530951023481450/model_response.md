```java
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TIOStreamTransport;

import java.io.InputStream;

public class ThriftReader {

    public ThriftReader(InputStream in, TProtocol protocol) {
        this.in = in;
        this.protocol = protocol;
    }

    private final InputStream in;
    private final TProtocol protocol;

    public void read() throws Exception {
        TIOStreamTransport transport = new TIOStreamTransport(in);
        protocol.readFrom(transport);
    }
}
```