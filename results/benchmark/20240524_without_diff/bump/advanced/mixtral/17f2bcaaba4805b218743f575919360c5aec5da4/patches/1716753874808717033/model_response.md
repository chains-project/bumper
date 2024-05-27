Here's the proposed patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_smooth() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

The fix consists of replacing `org.junit.Assume.assumeTrue(condition)` with `org.junit.jupiter.api.Assertions.assertTrue(condition)`.

The reason for this failure is that the `assumeTrue` method is part of the JUnit 4 library, while the test class is using JUnit Jupiter (JUnit 5) annotations.

`assumeTrue` is a method that checks the condition and if it's `false`, the test method is marked as 'skipped'. However, in JUnit 5, the equivalent functionality is provided by `org.junit.jupiter.api.Assertions.assertTrue(condition)`. This method checks the condition and if it's `false`, the test method will fail.

By using `assertTrue` instead of `assumeTrue`, the test method will fail if the condition is not met, and it will provide a meaningful error message.