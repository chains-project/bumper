```java
import org.apache.thrift.transport.TTransport;
```
Note: The repair is done by replacing `TFastFramedTransport` with `TTransport` which is a parent class of `TFastFramedTransport`.