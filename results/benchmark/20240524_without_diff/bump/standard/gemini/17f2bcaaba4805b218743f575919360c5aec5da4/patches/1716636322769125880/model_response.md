```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {

    private PGS_MorphologyGroupShape pgs_morphologyGroupShape;

    @BeforeEach
    public void setUp() {
        pgs_morphologyGroupShape = new PGS_MorphologyGroupShape();
    }

    @Test
    public void testGroupShape() {
        assertEquals(1, pgs_morphologyGroupShape.groupShape(new int[]{1, 2, 3}));
    }
}
```