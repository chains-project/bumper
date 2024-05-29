Here's the proposed patch:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The patch imports the `assertTrue` method from `org.junit.jupiter.api.Assertions` and uses it to replace the `org.junit.Assume.assumeTrue` method call. This should fix the "cannot find symbol" error.