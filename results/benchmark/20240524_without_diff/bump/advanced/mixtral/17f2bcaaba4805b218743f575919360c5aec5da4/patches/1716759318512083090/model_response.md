Here is a possible patch for the failing client code:
```java
import org.junit.Assert;

//...

assertEquals(expected, actual);
```
Explanation:
The error message suggests that there is a problem with the static import statement. To fix this, we can replace the static import with an import for the `Assert` class, and then use the `assertEquals` method as a regular method call. This should resolve the compilation error.