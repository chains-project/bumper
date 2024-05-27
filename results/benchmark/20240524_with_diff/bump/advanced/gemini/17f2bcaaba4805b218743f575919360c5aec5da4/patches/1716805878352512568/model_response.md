```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyVW() {
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyVW(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```