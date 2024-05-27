This error message is indicating that there is a syntax error in your code. Unfortunately, without the full context of your code, it's impossible to provide a specific fix. However, the error message is suggesting that a class, interface, or enum declaration is expected at the location of the error.

Given the import statement provided, it seems like you are trying to use JUnit 5 for testing. Here is a basic example of a test class in JUnit 5:

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {

    @Test
    public void testSomething() {
        assertEquals(1, 1);
    }
}
```

This code defines a class `PGS_MorphologyGroupShapeTests` with a single test method `testSomething`. The `@Test` annotation indicates that this method is a test case. The `assertEquals` method is a simple assertion that checks if two values are equal. If they are not, the test fails.