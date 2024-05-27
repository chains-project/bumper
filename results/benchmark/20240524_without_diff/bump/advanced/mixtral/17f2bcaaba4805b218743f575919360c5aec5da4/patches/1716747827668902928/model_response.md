Here's the fixed method with the proper import statement added:
```java
import static org.junit.jupiter.api.Assertions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_radialWarp() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```
The error was caused by the missing import statement for `assumeTrue`.