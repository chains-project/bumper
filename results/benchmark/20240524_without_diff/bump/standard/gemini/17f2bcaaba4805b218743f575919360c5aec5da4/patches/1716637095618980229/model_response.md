```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class PGS_MorphologyGroupShapeTests {

    @Test
    public void testMorphologyGroupShape() {
        // Given
        int[][] image = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1}
        };

        // When
        int[][] result = PGS_Morphology.groupShape(image);

        // Then
        int[][] expected = {
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1}
        };
        assertEquals(expected, result);
    }
}
```