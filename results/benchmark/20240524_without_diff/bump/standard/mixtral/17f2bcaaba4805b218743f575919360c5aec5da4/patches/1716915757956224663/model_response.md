Here's a proposed patch for the given failing client code:

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

The issue with the original code is that it uses `org.junit.Assume.assumeTrue`, which is not a method in JUnit 5. It should use `org.junit.jupiter.api.Assertions.assertTrue` instead.