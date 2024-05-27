Here is a proposed patch for the failing client code:

```java
import org.junit.Assert;

// ...

assertEquals(expected, actual);
```

In this patch, I have removed the static import statement and replaced it with an import statement for the `Assert` class. I have also removed the `static` keyword from the `assertEquals` method call. This should fix the error message you were seeing about static imports only being allowed for classes and interfaces.