Here is a proposed patch for the failing client code:
```java
import org.junit.Assert;
```

```java
assertEquals(expected, actual);
```
In this patch, we replace the static import statement with an import statement for the `Assert` class. We then use the `assertEquals` method directly on the `Assert` class. This should resolve the error message, which indicates that static imports are only allowed from classes and interfaces.