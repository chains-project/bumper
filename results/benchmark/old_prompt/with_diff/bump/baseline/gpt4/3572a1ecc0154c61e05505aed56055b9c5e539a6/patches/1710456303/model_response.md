```java
  import org.apache.thrift.transport.TIOStreamTransport;
  import org.apache.thrift.TConfiguration;

  // Replace TFastFramedTransport with TIOStreamTransport
  TConfiguration tConfiguration = new TConfiguration();
  TIOStreamTransport transport = new TIOStreamTransport(tConfiguration);
```