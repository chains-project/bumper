Here is a possible patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_smoothGaussian() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

This patch replaces the failing `assumeTrue` method with the `assertTrue` method, which has the same behavior but does not throw an error if the condition is not met. This should fix the error message about the missing symbol.