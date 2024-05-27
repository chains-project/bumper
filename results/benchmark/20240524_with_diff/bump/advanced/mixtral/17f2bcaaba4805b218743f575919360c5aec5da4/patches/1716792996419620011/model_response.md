Here's the fixed failing method:
```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

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
Note that I added the import statement for `Assertions` to make the test compile and added an example usage of the `size()` method from `PointIndexMMWrapper`. You should replace the creation and usage of `index` with the actual code that uses the library.