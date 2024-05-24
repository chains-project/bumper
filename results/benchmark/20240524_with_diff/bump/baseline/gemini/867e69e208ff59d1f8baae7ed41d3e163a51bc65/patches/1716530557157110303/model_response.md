```java
import org.apache.thrift.transport.TMemoryInputTransport;
import org.apache.thrift.transport.TNonblockingTransport;
import org.apache.thrift.transport.TTransport;

public class SimpleThriftLogger {

    public static void main(String[] args) {
        // Create a TMemoryInputTransport with the serialized data.
        byte[] serializedData = ...;
        TMemoryInputTransport transport = new TMemoryInputTransport(serializedData);

        // Create a TNonblockingTransport to wrap the TMemoryInputTransport.
        TNonblockingTransport nonblockingTransport = new TNonblockingTransport(transport);

        // Use the nonblockingTransport to read the data.
        // ...
    }
}
```