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
        // Given
        PGS_MorphologyGroupShape pgs_morphologyGroupShape = new PGS_MorphologyGroupShape();

        // When
        PGS_MorphologyGroupShape.GroupShape groupShape = pgs_morphologyGroupShape.groupShape();

        // Then
        assertEquals(PGS_MorphologyGroupShape.GroupShape.RECTANGLE, groupShape);
    }
}
```