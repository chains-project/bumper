```java
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class FastPolygonizerTests {

    @Test
    public void testPolygonize() {
        // Given
        double[][] points = {
                {0, 0},
                {1, 0},
                {1, 1},
                {0, 1}
        };

        // When
        Polygon polygon = new FastPolygonizer().polygonize(points);

        // Then
        assertEquals(4, polygon.getVertices().size());
        assertEquals(0, polygon.getVertices().get(0).getX(), 0.001);
        assertEquals(0, polygon.getVertices().get(0).getY(), 0.001);
        assertEquals(1, polygon.getVertices().get(1).getX(), 0.001);
        assertEquals(0, polygon.getVertices().get(1).getY(), 0.001);
        assertEquals(1, polygon.getVertices().get(2).getX(), 0.001);
        assertEquals(1, polygon.getVertices().get(2).getY(), 0.001);
        assertEquals(0, polygon.getVertices().get(3).getX(), 0.001);
        assertEquals(1, polygon.getVertices().get(3).getY(), 0.001);
    }
}
```