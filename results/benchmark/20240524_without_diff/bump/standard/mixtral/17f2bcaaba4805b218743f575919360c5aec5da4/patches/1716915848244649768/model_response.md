Here's the fixed code:
```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_radialWarp() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    assertEquals(2, out.getChildCount());
}
```
The issue was that the `Assume` class was not being imported statically, so the `assumeTrue` method was not found. By adding the import statement, the issue should be resolved.