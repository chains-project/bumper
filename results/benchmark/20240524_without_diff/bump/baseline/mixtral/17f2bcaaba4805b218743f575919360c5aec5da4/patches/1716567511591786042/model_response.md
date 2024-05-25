Here's a suggested patch for the failing client code:

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
        fail("minkSum returned a null shape.");
    }
}
```

In this patch, I added a null check for the `out` variable before calling `assertEquals`, and if `out` is null, the test will fail with a custom error message. This is to handle the case where the external dependency change might cause `minkSum` to return null, causing the "cannot find symbol" error when calling `getChildCount()` on a null object.