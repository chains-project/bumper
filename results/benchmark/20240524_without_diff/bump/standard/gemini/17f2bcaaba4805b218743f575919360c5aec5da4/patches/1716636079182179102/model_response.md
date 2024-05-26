```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class PGS_MorphologyGroupShapeTests {

    private PGS_MorphologyGroupShape pgs_morphologyGroupShape;

    @BeforeEach
    void setUp() {
        pgs_morphologyGroupShape = new PGS_MorphologyGroupShape();
    }

    @Test
    void testMorphologyGroupShape() {
        List<String> expected = List.of("circle", "square", "triangle");
        assertEquals(expected, pgs_morphologyGroupShape.getMorphologyGroupShape());
    }

    @Test
    void testMorphologyGroupShapeWithInvalidInput() {
        assertThrows(IllegalArgumentException.class, () -> pgs_morphologyGroupShape.getMorphologyGroupShape("invalid input"));
    }
}
```