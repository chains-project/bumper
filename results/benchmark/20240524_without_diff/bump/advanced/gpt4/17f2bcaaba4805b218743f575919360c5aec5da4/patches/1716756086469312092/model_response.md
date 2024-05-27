This error message indicates that there's a problem with the import statement. It seems to be floating without being attached to a class or interface. Here's a possible fix:

```java
public class PGS_MorphologyGroupShapeTests {
    import static org.junit.jupiter.api.Assertions.assertEquals;
}
```

However, please note that the import statement should be outside the class, not inside. The correct code should look like this:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {
    // your test methods here
}
```