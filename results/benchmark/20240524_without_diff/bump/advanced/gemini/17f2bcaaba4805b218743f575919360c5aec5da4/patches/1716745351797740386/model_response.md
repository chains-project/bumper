```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    org.junit.Assume.assumeThat(GROUP_SHAPE.getChildCount(), org.hamcrest.Matchers.is(2));
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```