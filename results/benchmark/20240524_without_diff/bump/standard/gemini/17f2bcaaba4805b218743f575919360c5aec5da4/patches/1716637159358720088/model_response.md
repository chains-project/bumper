```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.Arrays;
import java.util.List;

public class PGS_MorphologyGroupShapeTests {

    @org.junit.jupiter.api.Test
    public void testGroupShapes() {
        PGS pgs = new PGS();
        List<Shape> shapes = Arrays.asList(
                new Shape(1, 2, 3),
                new Shape(4, 5, 6),
                new Shape(7, 8, 9)
        );
        List<Shape> expected = Arrays.asList(
                new Shape(1, 2, 3),
                new Shape(4, 5, 6),
                new Shape(7, 8, 9)
        );
        assertEquals(expected, pgs.groupShapes(shapes));
    }
}
```