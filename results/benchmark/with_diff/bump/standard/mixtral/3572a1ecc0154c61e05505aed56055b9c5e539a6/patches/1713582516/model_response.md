Here's the proposed patch for the failing client code:

```java
@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    TConfiguration tConfiguration = new TConfiguration();
    TIOStreamTransport tIOStreamTransport = new TIOStreamTransport(tConfiguration, os);
    framedTransport = new TFastFramedTransport(tIOStreamTransport, bufferCapacity);
    protocol = new TBinaryProtocol(framedTransport);
}
```

The changes made include:

* Creating a `TConfiguration` object to be used in creating the `TIOStreamTransport` object.
* Using the new constructor for `TIOStreamTransport` that takes a `TConfiguration` object as a parameter.
* Creating the `TFastFramedTransport` object using the new constructor that takes a `TIOStreamTransport` object as a parameter.

These changes should allow the client code to work with the new library version.