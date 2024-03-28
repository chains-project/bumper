Based on the information provided, it seems the issue is caused by a missing symbol import. I will assume that the required class was removed from the Apache Thrift library and is no longer available. In this case, we need to replace the usage of `TFastFramedTransport` with an alternative that provides similar functionality.

Assuming that `TFramedTransport` from the same package provides similar functionality, you can replace the problematic line with the following:

```java
import org.apache.thrift.transport.TFramedTransport;
```

However, if the functionality of `TFastFramedTransport` is required, you may need to find a replacement library that provides similar functionality or implement the required functionality yourself.

Please note that this is just a suggested fix based on the provided information. In order to provide a more accurate solution, more information about the codebase and the specific functionality of `TFastFramedTransport` would be needed.