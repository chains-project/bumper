It seems like the import statement is failing because the compiler cannot find the TFramedTransport class in the org.apache.thrift.transport package. This could be due to a number of reasons such as:

1. The thrift library is not added in the classpath.
2. The version of thrift library being used does not contain TFramedTransport class.

To fix the issue, first, make sure that the thrift library is added in the classpath. If it's already in the classpath, then check the version of the thrift library being used. It's possible that the version you're using does not contain the TFramedTransport class. In that case, you need to upgrade or downgrade the library to a version that contains the TFramedTransport class.

If the library and its version are correct then there might be a problem with the import statement itself. 

Here is the corrected import statement:

```java
import org.apache.thrift.transport.TFramedTransport;
```

Please replace the existing import statement with the above line of code. If the problem still persists then there is definitely a problem with the library configuration and not the code.