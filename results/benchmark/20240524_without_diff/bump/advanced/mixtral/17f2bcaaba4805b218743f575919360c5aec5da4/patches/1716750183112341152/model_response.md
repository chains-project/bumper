Here's the proposed patch for the failing client code:

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

In this patch, we replace `org.junit.Assume.assumeTrue` with `org.junit.jupiter.api.Assertions.assertTrue` to avoid the "cannot find symbol" error.

Note: The `import static` statements are added for brevity and better readability. The code will work without them, but you will need to use the fully qualified names of the methods.