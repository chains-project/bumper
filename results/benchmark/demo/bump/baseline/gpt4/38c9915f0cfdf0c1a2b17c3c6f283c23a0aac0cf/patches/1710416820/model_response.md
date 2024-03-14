The error message indicates that the symbol `LengthOf` cannot be found. This is likely because the import statement is incorrect. 

The `LengthOf` class is not present in `org.cactoos.iterable` package. It is present in `org.cactoos.scalar` package. So, the correct import statement should be:

```java
import org.cactoos.scalar.LengthOf;
```