Here's the patched code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

The fix involves changing the `org.junit.Assume.assumeTrue` call to `org.junit.jupiter.api.Assertions.assertTrue`, as the former is not available in the current environment.