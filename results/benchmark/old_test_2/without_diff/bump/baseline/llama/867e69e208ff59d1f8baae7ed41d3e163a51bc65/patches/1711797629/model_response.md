Here's a proposed patch to fix the error:
```java
import org.apache.thrift.transport.TFramedTransport;

public class SimpleThriftLogger {
    private static final TFramedTransport.Factory factory = new TFramedTransport.Factory();

    public static void log(String message) {
        try (TFramedTransport transport = factory.getTransport()) {
            transport.open();
            transport.write(message.getBytes());
            transport.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
The issue is caused by the fact that the `TFramedTransport` class has been removed from the Apache Thrift library in version 0.12.0.
To fix the issue, we can use the `TFramedTransport.Factory` class to create a new instance of `TFramedTransport` and then use its `getTransport()` method to get a new transport instance.
We then use the `open()`, `write()`, and `flush()` methods to send the message over the wire.
Note that we've also removed the `Override` annotation, as it's not necessary in this case.