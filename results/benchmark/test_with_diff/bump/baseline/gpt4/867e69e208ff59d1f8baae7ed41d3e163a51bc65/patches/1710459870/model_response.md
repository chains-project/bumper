Based on the error message, it seems that the class `TFramedTransport` is no longer available in the `org.apache.thrift.transport` package. Unfortunately, without knowing the changes in the new library version, it's impossible to suggest a specific patch.

However, generally, if a class has been removed from a library, it's likely that it has been replaced with a new class or method. You would need to check the documentation for the new version of the Apache Thrift library to see what has replaced the `TFramedTransport` class.

For example, if `TFramedTransport` was replaced by a new class `TNewFramedTransport`, the import statement in your code would change from:

```java
import org.apache.thrift.transport.TFramedTransport;
```

to:

```java
import org.apache.thrift.transport.TNewFramedTransport;
```

Please replace `TNewFramedTransport` with the actual new class or method provided in the new version of the library.