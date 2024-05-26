```java
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {

    @Test
    public void testGroupShape() {
        // Given
        PGS pgs = new PGS();
        pgs.setGroupShape(PGS.GroupShape.RECTANGLE);

        // When
        PGS.GroupShape groupShape = pgs.getGroupShape();

        // Then
        assertEquals(PGS.GroupShape.RECTANGLE, groupShape);
    }
}
```