```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyVW() {
    org.junit.jupiter.api.Assumptions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyVW(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```