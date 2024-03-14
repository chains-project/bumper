The error message indicates that the symbol `IoCheckedScalar` cannot be found. This is likely because the import statement is incorrect or the library `org.cactoos.scalar.IoCheckedScalar` does not exist or has been moved in the updated version of the library.

Since I don't have information about the updated version of the library, I'll assume that the `IoCheckedScalar` class has been moved to a different package within the same library. 

A common practice in Java libraries is to move classes to a more specific package. In this case, the `IoCheckedScalar` class might have been moved to the `org.cactoos.scalar.io` package. 

Here is the corrected code:

```java
import org.cactoos.scalar.io.IoCheckedScalar;
```

Please replace the existing import statement with this one and try to compile the code again. If it still fails, you might need to check the updated library documentation to find the new location of the `IoCheckedScalar` class.