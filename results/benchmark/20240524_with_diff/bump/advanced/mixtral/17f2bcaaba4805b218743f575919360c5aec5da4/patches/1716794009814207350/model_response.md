Here's the proposed patch for the client code:
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {
    @Test
    public void testSize() {
        org.tinspin.index.PointIndexMMWrapper index = new org.tinspin.index.PointIndexMMWrapper();
        assertEquals(0, index.size());

        index.add(new double[]{1.0, 2.0});
        assertEquals(1, index.size());
    }
}
```
This patch adds a test method `testSize()` that creates an instance of `PointIndexMMWrapper`, adds a point to it, and checks the size of the index before and after adding the point. This test should pass if the `size()` method of `PointIndexMMWrapper` is implemented correctly.