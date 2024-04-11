Here's the proposed patch:

```java
@Override
public void init(OutputStream os) {
    this.os = os;
    TConfiguration tConfig = new TConfiguration();
    // Use the TFlushingFastFramedTransport to be compatible with singer_thrift log.
    final int bufferCapacity = 10;
    framedTransport = new TFastFramedTransport(new TIOStreamTransport(tConfig, os), bufferCapacity);
    protocol = new TBinaryProtocol(framedTransport);
}
```

The changes include:

* Importing `org.apache.thrift.transport.TIOStreamTransport` and `org.apache.thrift.TConfiguration`.
* Creating a `TConfiguration` object `tConfig`.
* Using `TIOStreamTransport` constructor with `TConfiguration` and `OutputStream` to create a new `TIOStreamTransport` object.
* Using the new `TIOStreamTransport` object to create a new `TFastFramedTransport` object.