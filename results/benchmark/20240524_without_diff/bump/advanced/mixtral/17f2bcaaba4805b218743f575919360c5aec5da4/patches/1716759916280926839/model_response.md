Here is the proposed patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Processing_removeSmallHoles() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Processing.removeSmallHoles(GROUP_SHAPE, 10);
    assertTrue(out.getChildCount() == 2);
}
```
In the original code, the method `assumeTrue` is used, but it is not a valid method in JUnit 5. Instead, I replaced it with `assertTrue`, which is the correct method to use in JUnit 5 to assert that a boolean condition is true.