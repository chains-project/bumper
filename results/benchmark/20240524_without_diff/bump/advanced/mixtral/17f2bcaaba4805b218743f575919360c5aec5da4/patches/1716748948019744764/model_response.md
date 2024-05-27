Here is a proposed patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_round() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

This patch imports the `assertTrue` method from `org.junit.jupiter.api.Assertions` and uses it in place of `Assume.assumeTrue` to avoid the "cannot find symbol" error.

Note that `Assume.assumeTrue` and `assertTrue` have slightly different behavior. `Assume.assumeTrue` will skip the current test if the condition is not met, while `assertTrue` will throw an `AssertionError` if the condition is not met. You may want to adjust the behavior of the test according to your needs.