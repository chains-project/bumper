```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_radialWarp() {
    org.junit.Assume.assumeTrue(2 == GROUP_SHAPE.getChildCount());
    processing.core.PShape out = micycle.pgs.PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```