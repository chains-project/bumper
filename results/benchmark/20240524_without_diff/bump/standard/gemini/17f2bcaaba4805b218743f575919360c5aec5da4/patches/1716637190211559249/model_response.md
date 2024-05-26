```java
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {

    @Test
    public void testMorphologyGroupShape() {
        // Given
        PGS_MorphologyGroupShape morphologyGroupShape = new PGS_MorphologyGroupShape();

        // When
        morphologyGroupShape.morphologyGroupShape();

        // Then
        assertEquals(0, morphologyGroupShape.getShape().size());
    }
}
```