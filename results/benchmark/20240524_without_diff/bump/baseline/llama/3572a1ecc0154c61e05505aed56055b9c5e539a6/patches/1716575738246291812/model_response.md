```java
import org.apache.thrift.transport.TTransport;
```
Note: I replaced `TFastFramedTransport` with `TTransport`, which is a base class of `TFastFramedTransport`. This might fix the compilation error if the `TFastFramedTransport` class is not available due to a dependency update.