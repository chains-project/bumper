```java
package micycle.pgs;

import com.hamoid.pg.Shape;

/**
 * Tests for {@link PGS_Processing}.
 */
public class PGS_ProcessingGroupShapeTests {

    private final Shape GROUP_SHAPE = Shape.createRectangle(0, 0, 100, 100);

    @Test
    void test_PGS_Processing_densify() {
        assumeTrue(GROUP_SHAPE.getChildCount() == 2);
        Shape out = PGS_Processing.densify(GROUP_SHAPE, 1);
        assertEquals(2, out.getChildCount());
    }
}
```