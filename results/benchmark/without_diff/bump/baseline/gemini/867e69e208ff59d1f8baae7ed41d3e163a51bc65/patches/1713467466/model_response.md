```java
import org.apache.thrift.transport.TTransport;

public class ThriftReader {

    public void read() throws Exception {
        // Create a new TFramedTransport object using the underlying socket.
        TTransport transport = new TFramedTransport(socket);

        // Create a new Thrift protocol object using the transport.
        TProtocol protocol = new TBinaryProtocol(transport);

        // Create a new Thrift client object using the protocol.
        ThriftClient client = new ThriftClient(protocol);

        // Read data from the Thrift server.
        client.readData();

        // Close the transport.
        transport.close();
    }
}
```