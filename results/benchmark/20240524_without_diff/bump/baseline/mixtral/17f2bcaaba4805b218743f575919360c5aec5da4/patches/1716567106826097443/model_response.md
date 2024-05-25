Here is a possible patch for the failing client code:

```java
import processing.core.PApplet;
import processing.core.PShape;
import static processing.core.PConstants.CLOSE;

public class PGS_MorphologyGroupShapeTests {

    // ... other code ...

    @Test
    void test_PGS_Morphology_minkDifference() {
        assumeTrue(GROUP_SHAPE.getChildCount() == 2);
        final PShape mink = new PShape(PShape.PATH);
        PApplet.runSketch(new Sketch() {
            @Override
            public void settings() {
                size(100, 100);
            }

            @Override
            public void draw() {
                background(255);
                mink.beginShape();
                mink.vertex(0, 0);
                mink.vertex(5, 0);
                mink.vertex(5, 5);
                mink.vertex(0, 5);
                mink.endShape(CLOSE);
            }
        });

        PShape out = PGS_Morphology.minkDifference(GROUP_SHAPE, mink);
        assertEquals(2, out.getChildCount());
    }

    // ... other code ...

    static class Sketch extends PApplet {
    }
}
```

This patch creates a new nested class `Sketch` that extends `PApplet`, and moves the creation of the `mink` shape to its `draw` method. This way, the `mink` shape is created within a `PApplet` context, which should fix the "cannot find symbol" error. Note that this patch assumes that the `PGS_Morphology` class and the `GROUP_SHAPE` variable are defined elsewhere in the code, and that they are not causing the error.