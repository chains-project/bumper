```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_minkDifference() {
    org.junit.jupiter.api.Assumptions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    final processing.core.PShape mink = new processing.core.PShape(processing.core.PShape.PATH);
    mink.beginShape();
    mink.vertex(0, 0);
    mink.vertex(5, 0);
    mink.vertex(5, 5);
    mink.vertex(0, 5);
    mink.endShape(processing.core.PConstants.CLOSE);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.minkDifference(GROUP_SHAPE, mink);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```