```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_radialWarp() {
    if (GROUP_SHAPE.getChildCount() != 2) {
        return;
    }
    processing.core.PShape out = micycle.pgs.PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```