Here's the fixed version of the code:
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
The issue was that the `assumeTrue` method was not being imported. I added the import statement for it and now the code should compile and run successfully.