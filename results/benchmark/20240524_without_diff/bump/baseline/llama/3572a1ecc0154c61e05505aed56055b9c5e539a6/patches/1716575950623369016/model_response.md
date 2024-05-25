```java
import org.apache.thrift.transport.TTransport;
```
Note: The `TFastFramedTransport` class has been removed in newer versions of Apache Thrift. It has been replaced with `TFramedTransport`. However, since we cannot use removed library methods, we can use the `TTransport` interface instead, which is a superclass of `TFastFramedTransport`.