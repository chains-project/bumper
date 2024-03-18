The error message indicates that the class `TFramedTransport` cannot be found in the package `org.apache.thrift.transport`. This could be due to the class being moved, renamed, or removed in the updated library version. 

Without the information about the changes in the new library version, it's hard to propose a specific fix. However, assuming that the class has been renamed or moved, the fix would involve updating the import statement to match the new class name or location.

For example, if the class `TFramedTransport` has been renamed to `TBufferedTransport`, the updated code would be:

```java
  import org.apache.thrift.transport.TBufferedTransport;
```

Or if the class has been moved to a different package, for example `org.apache.thrift.newtransport`, the updated code would be:

```java
  import org.apache.thrift.newtransport.TFramedTransport;
```

Please replace `TBufferedTransport` and `org.apache.thrift.newtransport` with the actual new class name or package.