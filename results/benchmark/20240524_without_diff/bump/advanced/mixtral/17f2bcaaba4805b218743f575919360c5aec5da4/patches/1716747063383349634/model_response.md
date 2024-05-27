Here's a fixed version of the code that uses `org.junit.jupiter.api.Assertions.assertTrue` instead of `org.junit.Assume.assumeTrue`:
```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_minkSum() {
    org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2);
    final processing.core.PShape mink = new processing.core.PShape(processing.core.PShape.PATH);
    mink.beginShape();
    mink.vertex(0, 0);
    mink.vertex(5, 0);
    mink.vertex(5, 5);
    mink.vertex(0, 5);
    mink.endShape(processing.core.PConstants.CLOSE);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.minkSum(GROUP_SHAPE, mink);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```
The reason for the error is that the `assumeTrue` method is not available in the `org.junit.jupiter.api.Assertions` class. The `assertTrue` method should be used instead.