```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_radialWarp() {
    org.junit.Assume.assumeThat(GROUP_SHAPE.getChildCount(), org.hamcrest.Matchers.equalTo(2));
    processing.core.PShape out = micycle.pgs.PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```