Here's the modified version of the client code that should resolve the error:
```java
import org.junit.Assert;

// ...

assertEquals("Ensure the message is as expected", expectedMessage, actualMessage);
```
By removing the static import and using the fully qualified class name, the error should be resolved.