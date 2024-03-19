@java.lang.Override
public void init(java.io.OutputStream os) {
    this.os = os;
    final int bufferCapacity = 10;
    // Replace TFastFramedTransport with TFramedTransport
    framedTransport = new org.apache.thrift.transport.TFramedTransport(new org.apache.thrift.transport.TIOStreamTransport(os), bufferCapacity);
    protocol = new org.apache.thrift.protocol.TBinaryProtocol(framedTransport);
}