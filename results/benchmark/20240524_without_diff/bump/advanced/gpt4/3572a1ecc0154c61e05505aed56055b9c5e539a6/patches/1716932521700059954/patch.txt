@java.lang.Override
protected org.apache.thrift.TSerializer initialValue() {
    try {
        return new org.apache.thrift.TSerializer(new org.apache.thrift.protocol.TCompactProtocol.Factory());
    } catch (org.apache.thrift.transport.TTransportException e) {
        throw new RuntimeException(e);
    }
}