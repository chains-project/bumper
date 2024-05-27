Here's the fixed `test_PGS_Morphology_round` method with the necessary import statement added:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The issue was caused by using `org.junit.Assume.assumeTrue` instead of `org.junit.jupiter.api.Assertions.assertTrue`. I replaced the former with the latter to resolve the error.