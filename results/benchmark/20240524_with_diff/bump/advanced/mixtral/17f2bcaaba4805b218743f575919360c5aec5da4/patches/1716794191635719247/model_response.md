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

        index.add(new double[]{1.0, 2.0});
        expectedSize = 1;
        assertEquals(expectedSize, index.size());

        index.add(new double[]{3.0, 4.0});
        expectedSize = 2;
        assertEquals(expectedSize, index.size());
    }
}
```
This code adds a new test method `testSize()` that creates an instance of `PointIndexMMWrapper` and checks its size after adding some elements to it. This should fix the error by using the newly added `size()` method in the updated library version.