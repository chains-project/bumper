Here's a proposed patch to fix the error:
```java
import org.apache.thrift.transport.TFramedTransport;

public class SimpleThriftLogger {
    private final TFramedTransport.Factory transportFactory;

    public SimpleThriftLogger(TFramedTransport.Factory transportFactory) {
        this.transportFactory = transportFactory;
    }

    public void log(String message) {
        try (TFramedTransport transport = transportFactory.getTransport()) {
            transport.open();
            transport.write(message);
            transport.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
The error is caused by the fact that the `TFramedTransport` class has been removed from the Apache Thrift library. To fix this, we can replace the import statement with the following:
```java
import org.apache.thrift.transport.TTransport;
```
We can also remove the `TFramedTransport.Factory` class, as it is no longer needed. Here's the updated code:
```java
import org.apache.thrift.transport.TTransport;

public class SimpleThriftLogger {
    private final TTransport transport;

    public SimpleThriftLogger(TTransport transport) {
        this.transport = transport;
    }

    public void log(String message) {
        try {
            transport.open();
            transport.write(message);
            transport.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
This code should now compile without any errors related to the `TFramedTransport` class.