Here's the fixed version of the client code, which removes the problematic static import statement:

```java
import org.junit.Assert;

// ...

assertEquals("message", expected, actual);
```

This version imports the `Assert` class directly and uses the fully qualified method name in the `assertEquals` method call.