Here is a possible patch for the failing client code:
```java
import processing.core.PShape;
import static processing.core.PConstants.*;

@Test
void test_PGS_Morphology_minkDifference() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape mink = new PShape(PATH);
    mink.beginShape();
    mink.vertex(0, 0);
    mink.vertex(5, 0);
    mink.vertex(5, 5);
    mink.vertex(0, 5);
    mink.endShape(CLOSE);

    PShape out = PGS_Morphology.minkDifference(GROUP_SHAPE, mink);
    assertEquals(2, out.getChildCount());
}
```
The changes I made to the original code are:

* I replaced `PShape.PATH` with `PATH`, and `PConstants.CLOSE` with `CLOSE`. This is because the `PShape` and `PConstants` classes were not imported in the original code, but their members were used. To avoid using the fully qualified names, I added the necessary imports.
* I also added the missing import statements for `PShape` and `PConstants`.

These changes should fix the "cannot find symbol" error.