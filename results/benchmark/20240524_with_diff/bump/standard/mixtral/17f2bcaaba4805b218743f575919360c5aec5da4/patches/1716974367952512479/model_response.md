Here's a patch that you can apply to the failing client code:
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {
    @Test
    public void testSize() {
        org.tinspin.index.PointIndexMMWrapper index = new org.tinspin.index.PointIndexMMWrapper();
        int expectedSize = 0;
        int actualSize = index.size();
        assertEquals(expectedSize, actualSize);
    }
}
```
This code creates a new instance of `PointIndexMMWrapper` and checks its size using the new `size()` method. The `assertEquals()` method is used to verify that the expected size (which is initially set to 0) is equal to the actual size of the index.