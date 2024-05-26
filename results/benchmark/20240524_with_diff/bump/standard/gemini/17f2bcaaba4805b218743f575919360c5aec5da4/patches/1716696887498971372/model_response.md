```java
import static org.junit.Assert.assertEquals;

public class PGS_MeshingTests {

    @org.junit.Test
    public void testMeshing() {
        // Arrange
        PGS pgs = new PGS();

        // Act
        Mesh mesh = pgs.mesh();

        // Assert
        assertEquals(10, mesh.getVertices().size());
        assertEquals(20, mesh.getEdges().size());
        assertEquals(30, mesh.getFaces().size());
    }
}
```