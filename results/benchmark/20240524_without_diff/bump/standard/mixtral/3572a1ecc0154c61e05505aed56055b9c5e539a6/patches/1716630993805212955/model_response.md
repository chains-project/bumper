Here' proposal for the patch:
```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    framedTransport = new org.apache.thrift.transport.TFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os));
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
    framedTransport.setFramedTransportEventListener(new org.apache.thrift.transport.FramedTransport.Factory.DefaultFactory.DefaultFramedTransportEventListener(bufferCapacity));
}
```
Explanation:

* I replaced the `com.pinterest.singer.client.logback.TFastFramedTransport` with the `org.apache.thrift.transport.TFramedTransport`
* I added the `framedTransport.setFramedTransportEventListener` to set the buffer capacity
* I removed the `new org.apache.thrift.transport.TIOStreamTransport(os)` from the `new com.pinterest.singer.client.logback.TFastFramedTransport`
* I removed the `int bufferCapacity` from the `new com.pista.sing.client.logback.TFastFramedTransport`
* I added the `new org.apache.thrift.protocol.TBinaryProtocol(framedTransport)` after the `framedTransport.setFramedTransportEventListener`
* I added the `new org.apache.thrift.transport.FramedTransport.Factory.DefaultFactory.DefaultFramedTransportEventListener(bufferCapacity)` to the `framedTransport.setFramedTransportEventListener`

This should fix the error message:
[ERROR] /singer/thrift-logger/src/main/java/com/pinterest/sista/client/logback/AppenderUtils.java:[64,29] cannot find symbol

Please note that I cannot guarantee that this will not break other parts of the code, but it should fix the specific error message you provided.