```java
import static org.junit.Assert.assertEquals;

public class PGS_MeshingTests {

    @Test
    public void testMeshing() {
        // Given
        Mesh mesh = new Mesh();

        // When
        mesh.mesh();

        // Then
        assertEquals(10, mesh.getVertices().size());
        assertEquals(20, mesh.getTriangles().size());
    }

}
```