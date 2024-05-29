Here's the fixed code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_fieldWarp() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.fieldWarp(GROUP_SHAPE, 10, 1, false);
    assertEquals(2, out.getChildCount());
}
```

The issue is caused by the use of `org.junit.Assume.assumeTrue` instead of `org.junit.jupiter.api.Assertions.assertTrue`. I have replaced the former with the latter.

Note that the import statement for `assertTrue` has been added, and the import for `Assertions.assertEquals` has been changed to use a static import. This makes the code more concise.