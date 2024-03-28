It appears that the issue is due to a missing or incorrect import statement. The symbol cannot be found because the compiler does not know where to look for it. 

If the `TFramedTransport` class is in a different package in the version of the library you are using, you will need to update the import statement to reflect this. 

If the class has been removed from the library, you will need to find a replacement or workaround. 

Without knowing the exact details of the library changes, it's difficult to provide a specific solution. 

However, as a generic solution, you could try to replace the import statement with the correct one. 

```java
import org.apache.thrift.transport.TTransport;
```

Please replace `TTransport` with the correct class name according to the library you are using.