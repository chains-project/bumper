```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_chaikinCut() {
    processing.core.PShape out = micycle.pgs.PGS_Morphology.chaikinCut(GROUP_SHAPE, 0.5, 2);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```