```java
package micycle.pgs;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assume.assumeTrue;

// ...

/**
 * Tests to verify the functionality of the {@link PGS_MorphologyGroupShape} class and its related classes.
 */
public class PGS_MorphologyGroupShapeTests extends PGS_MorphologyGroupTests {

    private static final double EPS = 1e-6;

    // ...

    private static boolean checkSize(String message, double expected, double actual) {
        return assertEquals(message, expected, actual, EPS);
    }

    // ...

    @Test
    public void size() {
        assumeTrue(hasPHTree());

        PGS_MorphologyGroupShape pg = new PGS_MorphologyGroupShape(new double[][]{
                {1, 4}, {2, 5}, {3, 7}
        });
        assertEquals(3, pg.size());  // Test that this method has been fixed.
    }

    // ...
}
```