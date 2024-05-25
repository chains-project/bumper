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
The changes I made are:

* Replace `PShape.PATH` with `PATH`
* Replace `PConstants.CLOSE` with `CLOSE`

This should fix the error message `cannot find symbol` by using the correct constant names.

Note that the constants `PATH` and `CLOSE` are added in Processing 3.4.0, so if the client code is using an older version of Processing, these constants may not be available. In this case, the client code needs to use the full name `PShape.PATH` and `PConstants.CLOSE` instead.