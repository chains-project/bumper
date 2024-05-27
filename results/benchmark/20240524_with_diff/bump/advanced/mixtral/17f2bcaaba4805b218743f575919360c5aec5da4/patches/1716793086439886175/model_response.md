Here is a proposed patch for the failing client code:
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {
    @Test
    public void testSize() {
        org.tinspin.index.PointIndexMMWrapper index = new org.tinspin.index.PointIndexMMWrapper();
        assertEquals(0, index.size());

        index.add(new double[] {1.0, 2.0});
        assertEquals(1, index.size());

        index.add(new double[] {3.0, 4.0});
        assertEquals(2, index.size());
    }
}
```
This code adds a new test method `testSize` that creates an instance of `org.tinspin.index.PointIndexMMWrapper`, adds some points to it, and checks the size of the index after each addition. This should fix the error by using the newly added `size()` method in the external dependency.