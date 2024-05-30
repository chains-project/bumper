Here's a fixed version of the client code that should resolve the error:
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
The error was caused by the missing import statement for the JUnit test annotation. I added a static import for `assertEquals` to make the code more concise.

I also added a simple test case using the `PointIndexMMWrapper` class, which has a `size()` method that was added in the new library version. The test case initializes an empty index, adds two points, and checks that the size of the index is correct after each addition.