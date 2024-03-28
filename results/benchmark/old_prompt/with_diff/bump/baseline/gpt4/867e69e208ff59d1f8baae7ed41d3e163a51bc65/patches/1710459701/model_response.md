Based on the error message, it seems like the class `TFramedTransport` is no longer available in the `org.apache.thrift.transport` package. Without information on the changes in the new library version, it's hard to propose a specific patch. 

However, if the `TFramedTransport` class has been moved to a different package, the import statement can be updated accordingly. 

For example, if `TFramedTransport` is now in the `org.apache.thrift.newtransport` package, the import statement would be:

```java
import org.apache.thrift.newtransport.TFramedTransport;
```

If the `TFramedTransport` class has been renamed or replaced with a different class, the import statement and any usage of `TFramedTransport` in the code should be updated with the new class name. 

For example, if `TFramedTransport` has been replaced with `TNewFramedTransport`, the import statement would be:

```java
import org.apache.thrift.transport.TNewFramedTransport;
```

And any usage of `TFramedTransport` in the code should be replaced with `TNewFramedTransport`.

Please check the documentation of the new library version to find the correct package or class to use.