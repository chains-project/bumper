Here's a proposed patch for the failing client code:

```java
import processing.core.PApplet;
import processing.core.PShape;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class PGS_MorphologyGroupShapeTests {
    // ... other code ...

    @Test
    void test_PGS_Morphology_minkDifference() {
        assumeTrue(GROUP_SHAPE.getChildCount() == 2);
        PApplet.runSketch(new String[]{}, () -> {
            final PShape mink = new PShape(PShape.PATH);
            mink.beginShape();
            mink.vertex(0, 0);
            mink.vertex(5, 0);
            mink.vertex(5, 5);
            mink.vertex(0, 5);
            mink.endShape(PConstants.CLOSE);

            PShape out = PGS_Morphology.minkDifference(GROUP_SHAPE, mink);
            assertEquals(2, out.getChildCount());
        });
    }
}
```

The patch introduces a `PApplet` instance using the `runSketch` method to create the required `PShape` instance. This should resolve the "cannot find symbol" error.