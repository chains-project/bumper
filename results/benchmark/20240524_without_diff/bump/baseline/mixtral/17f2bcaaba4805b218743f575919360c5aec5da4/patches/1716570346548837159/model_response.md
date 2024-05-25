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

* I imported the missing classes `PShape` and `PConstants` at the beginning of the file.
* I replaced the string literals `"PATH"` and `"CLOSE"` with their corresponding constants `PATH` and `CLOSE`.

These changes should fix the "cannot find symbol" error and make the code compile and run successfully.