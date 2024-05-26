Here's the updated code that uses TFramedTransport from the same package as TSocket:

```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    org.apache.thrift.transport.TSocket transport = null;
    try {
        transport = new org.apache.thrift.transport.TSocket("localhost", 9090);
        org.apache.thrift.transport.TFramedTransport framedTransport = new org.apache.thrift.transport.TFramedTransport(transport);
        framedTransport.open();
        return new org.apache.thrift.TDeserializer(new org.apache.thrift.protocol.TCompactProtocol(framedTransport));
   9  } catch (org.apache.thrift.transport.TTransportException e) {
        throw new java.lang.RuntimeException(e);
    } finally {
        if (transport != null) {
            transport.close();
        }
    }
}
```

In this updated code, I created a new variable `framedTransport` to wrap the `TSocket` with `TFramedTransport`. This way, we avoid the error caused by the missing `TFramedTransport` class.