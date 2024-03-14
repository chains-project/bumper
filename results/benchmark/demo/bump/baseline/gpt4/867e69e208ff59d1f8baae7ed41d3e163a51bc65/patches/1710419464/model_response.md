It seems like the error message "cannot find symbol" indicates that the Apache Thrift library is not properly imported. There could be several reasons for this: the library might not be in the classpath, the library might not be installed, or there might be a typo in the import statement. 

Since I can only work on the client code, I would suggest to first check if the Apache Thrift library is correctly installed and added to the classpath. If this is the case, then the issue might be a typo in the import statement. 

The import statement seems to be correct, so a possible solution could be to import the entire org.apache.thrift.transport package instead of just the TFramedTransport class:

```java
import org.apache.thrift.transport.*;
```

This will import all classes in the org.apache.thrift.transport package, including the TFramedTransport class. If there are other classes in the package that are used in the client code, they will also be imported. 

Please note that this solution assumes that the Apache Thrift library is correctly installed and added to the classpath. If this is not the case, the error will persist.