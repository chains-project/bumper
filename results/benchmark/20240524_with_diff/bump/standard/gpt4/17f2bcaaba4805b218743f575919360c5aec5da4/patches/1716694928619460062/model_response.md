The error message indicates that the import statement is incorrect because it's trying to statically import from a method rather than a class or interface. The correct code would be:

```java
import org.junit.Assert;
```

Then, in the code where `assertTrue` is used, you should call it as `Assert.assertTrue`.