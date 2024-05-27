Here's the proposed patch for the failing client code:
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {
    @Test
    public void testSize() {
        org.tinspin.index.PointIndexMMWrapper index = new org.tinspin.index.PointIndexMMWrapper();
        int expectedSize = 0;
        assertEquals(expectedSize, index.size());

        index.add(new double[] {1.0, 2.0});
        expectedSize = 1;
        assertEquals(expectedSize, index.size());

        index.add(new double[] {3.0, 4.0});
        expectedSize = 2;
        assertEquals(expectedSize, index.size());
    }
}
```
This patch adds a new test method `testSize()` that creates an instance of `PointIndexMMWrapper`, adds some points to it, and checks the size of the index after each addition. This should fix the error caused by the missing dependency update.