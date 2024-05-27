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

This patch replaces the failing `org.junit.Assume.assumeTrue` call with an equivalent `org.junit.jupiter.api.Assertions.assertTrue` call. This should fix the "cannot find symbol" error.

Note that this patch assumes that the `GROUP_SHAPE` variable is defined and accessible in the scope of the `test_PGS_Morphology_round` method. If this is not the case, the patch may need to be modified accordingly.