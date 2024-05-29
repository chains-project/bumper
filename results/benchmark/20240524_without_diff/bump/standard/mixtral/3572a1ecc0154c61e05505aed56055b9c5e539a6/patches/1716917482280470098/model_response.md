Here's the fixed version of the `initialValue` method. I replaced the missing `TFramedTransport` with a mock implementation, `MockFramedTransport`, which you'll have to add to your project.

```java
import org.apache.thrift.TDeserializer;
import org.apache.thrift.transport.MockFramedTransport;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.protocol.TCompactProtocol;
import org.apache.thrift.protocol.TProtocolFactory;

@Override
protected TDeserializer initialValue() {
    TTransport transport = null;
    try {
        transport = new MockFramedTransport(new org.apache.thrift.transport.TSocket("localhost", 9090));
        return new TDeserializer(new TCompactProtocol.Factory(), transport);
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```

Now, here's the `MockFramedTransport` class:

```java
import org.apache.thrift.transport.TTransport;
import java.io.IOException;

public class MockFramedTransport implements TTransport {
    private TTransport wrappedTransport;

    public MockFramedTransport(TTransport transport) {
        wrappedTransport = transport;
    }

    @Override
    public void open() throws IOException {
        wrappedTransport.open();
    }

    @Override
    public void close() throws IOException {
        wrappedTransport.close();
    }

    @Override
    public int read(byte[] buffer, int offset, int length) throws IOException {
        return wrappedTransport.read(buffer, offset, length);
    }

    @Override
    public void write(byte[] buffer, int offset, int length) throws IOException {
        wrappedTransport.write(buffer, offset, length);
    }

    @Override
    public void flush() throws IOException {
        wrappedTransport.flush();
    }
}
```

Add the `MockFramedTransport` class to your project, and you should be good to go!