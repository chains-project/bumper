Here's the proposed patch:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_smooth() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

The patch imports the missing `assertTrue` method from `org.junit.jupiter.api.Assertions` and replaces the `Assume.assumeTrue` method with `assertTrue`. This should resolve the "cannot find symbol" error.