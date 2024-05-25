```java
import org.apache.thrift.transport.TTransport;
```
Note: The `TFastFramedTransport` class has been removed in newer versions of Apache Thrift. It has been replaced with `TFramedTransport`. However, since you can only modify the client code, we can only use the `TTransport` interface which is still available.