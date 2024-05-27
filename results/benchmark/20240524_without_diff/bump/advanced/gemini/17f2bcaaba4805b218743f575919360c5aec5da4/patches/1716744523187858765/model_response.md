```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_chaikinCut() {
    org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.chaikinCut(GROUP_SHAPE, 0.5, 2);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```