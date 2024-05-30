Here's a patch for the failing client code:
```java
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class PGS_MorphologyGroupShapeTests {
    // Add a variable to store the size of the PointIndexMMWrapper
    private int pointIndexSize;

    @BeforeEach
    public void setUp() {
        // Initialize the PointIndexMMWrapper and get its size
        org.tinspin.index.PointIndexMMWrapper pointIndex = new org.tinspin.index.PointIndexMMWrapper();
        pointIndexSize = pointIndex.size();

        // Add assertions to check if the PointIndexMMWrapper has been initialized correctly
        assertTrue(pointIndexSize > 0);
    }
}
```
This patch creates a variable `pointIndexSize` to store the size of the `PointIndexMMWrapper` object and initializes it in the `setUp()` method. It also adds an assertion to check if the `PointIndexMMWrapper` has been initialized correctly. This should fix the error caused by the external dependency update.