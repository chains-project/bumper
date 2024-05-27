Here is the fixed version of the client code:
```java
import org.junit.Assert;

// ...

assertEquals(expected, actual);
```
Explanation:
The error message indicates that the static import statement is only allowed for classes and interfaces. In this case, we can simply remove the static import statement and use the fully qualified name of the `assertEquals` method instead.