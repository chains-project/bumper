It seems like the library that contains the class `TFramedTransport` was not imported correctly or does not exist in the classpath. You need to ensure that the correct version of the Apache Thrift library is included in your project.

If the library is correctly installed and the error persists, it may be due to an incorrect import statement. Verify that the class `TFramedTransport` is in the package `org.apache.thrift.transport`. If it's not, you would need to correct the import statement to the correct package.

Without the specific details about the project setup and the Apache Thrift library version, it's hard to provide a more specific solution. However, assuming that the issue is caused by an incorrect import statement, you can try to replace the import statement with the correct one.

In this case, I'm assuming that you're using a different version of the Apache Thrift library where the `TFramedTransport` class is located in the `org.apache.thrift.transport.layered` package. Here is the corrected code:

```java
import org.apache.thrift.transport.layered.TFramedTransport;
```

Please replace the existing import statement with the above line and see if it resolves the issue. If the error persists, please provide more details about the version of Apache Thrift library you're using and the project setup.