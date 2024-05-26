```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```