This error message suggests that there's a problem with the import statement itself, not with the code that uses the imported class. In this case, it appears that the import statement is not inside a class, interface, or enum, which is a requirement in Java.

Here is a generic example of how you could structure your code to avoid this error:

```java
public class PGS_MorphologyGroupShapeTests {
    import processing.core.PConstants;

    // your code here
}
```

Please replace "// your code here" with the actual code you're working on.