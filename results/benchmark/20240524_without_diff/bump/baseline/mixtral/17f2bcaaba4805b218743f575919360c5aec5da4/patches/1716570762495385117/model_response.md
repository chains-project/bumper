Here's a proposed patch for the failing client code:

```java
import processing.core.PShape;
import static processing.core.PConstants.CLOSE;

@Test
void test_PGS_Morphology_minkSum() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    final PShape mink = new PShape(PShape.PATH);
    mink.beginShape();
    mink.vertex(0, 0);
    mink.vertex(5, 0);
    mink.vertex(5, 5);
    mink.vertex(0, 5);
    mink.endShape(CLOSE);

    PShape out = PGS_Morphology.minkSum(GROUP_SHAPE, mink);
    if (out != null) {
        assertEquals(2, out.getChildCount());
    } else {
        fail("Expected a non-null result.");
    }
}
```

The patch includes a null check for the `out` variable, as the error message suggests that the symbol cannot be found, which could mean that `out` is null. The `fail()` method is called if `out` is null, causing the test to fail. This should help identify the root cause of the error.