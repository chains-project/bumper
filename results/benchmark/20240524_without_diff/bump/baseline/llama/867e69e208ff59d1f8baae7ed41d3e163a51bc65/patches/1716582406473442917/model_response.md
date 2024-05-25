```java
import org.apache.thrift.transport.TTransport;
```

(Note: I replaced `TFramedTransport` with `TTransport`, which is a parent class of `TFramedTransport` and is likely to be compatible with the existing code)