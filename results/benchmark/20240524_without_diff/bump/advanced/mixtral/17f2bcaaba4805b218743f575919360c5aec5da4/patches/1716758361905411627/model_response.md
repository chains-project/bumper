Here's the fixed version of the client code:
```java
import org.junit.Assert;

// ...

assertEquals(expected, actual);
```
Explanation:
The issue is caused by using a static import statement for a method. Instead, we should use the class name to access the method. In this case, we remove the static import statement and replace the method call with `Assert.assertEquals(expected, actual);`.