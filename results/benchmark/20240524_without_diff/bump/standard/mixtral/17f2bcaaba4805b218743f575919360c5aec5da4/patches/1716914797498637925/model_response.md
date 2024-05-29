Here's a fixed version of the code that replaces the failing method:

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

The fix involves replacing `org.junit.Assume.assumeTrue` with `org.junit.jupiter.api.Assertions.assertTrue`, since the former is not available in JUnit 5. The `assertTrue` method has the same behavior as `assumeTrue`, so the test should still work as expected.