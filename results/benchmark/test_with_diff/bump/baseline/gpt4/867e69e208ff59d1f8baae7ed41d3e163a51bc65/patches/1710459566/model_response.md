Based on the error message, it appears that the class `TFramedTransport` is no longer available in the `org.apache.thrift.transport` package. However, without knowing what the new library version includes, I can't provide a specific solution. 

In general, if a class has been removed from a library, you have a few options:

1. Find an equivalent class in the updated library and replace the import statement and any references to the old class with the new class. 

2. If no equivalent class exists, you may need to refactor your code to no longer rely on that class.

3. If the class is essential to your code and there's no alternative, you might need to revert to an older version of the library that still includes the class.

Without knowing the specific changes in the new library version, I can't provide a concrete solution. However, I can provide a general template for the first option:

```java
import org.apache.thrift.transport.NewEquivalentClass;
```

Replace `NewEquivalentClass` with the name of the new class that performs the same function as `TFramedTransport`. If no such class exists, further refactoring will be necessary.