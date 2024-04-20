@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    // Use the TFlushingFastFramedTransport to be compatible with singer_thrift
    // log.
    final int bufferCapacity = 10;
    org.apache.thrift.TConfiguration tConfiguration = new org.apache.thrift.TConfiguration();
    org.apache.thrift.transport.TIOStreamTransport tIOStreamTransport = new org.apache.thrift.transport.TIOStreamTransport(tConfiguration, os);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(tIOStreamTransport);
}