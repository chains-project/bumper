Here is a potential patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_simplify() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplify(GROUP_SHAPE, 1);
    assertEquals(2, out.getChildCount());
}
```

This patch uses the `assertTrue` method from `org.junit.jupiter.api.Assertions` instead of `org.junit.Assume.assumeTrue` to check the condition `GROUP_SHAPE.getChildCount() == 2`. This should fix the "cannot find symbol" error. Note that `assertTrue` will throw an exception if the condition is not true, which is the desired behavior in a unit test.