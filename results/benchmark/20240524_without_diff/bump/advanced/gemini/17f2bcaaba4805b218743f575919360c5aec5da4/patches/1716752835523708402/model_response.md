```java
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;

import micycle.pgs.PGS_Meshing;

public class PGS_MeshingTests {

    private static final double EPS = 1e-6;

    @Test
    public void testMeshing() {
        // Create a PGS meshing object
        PGS_Meshing meshing = new PGS_Meshing();

        // Set the meshing parameters
        meshing.setMeshSize(1.0);
        meshing.setMeshResolution(10);

        // Create a list of points
        List<double[]> points = Arrays.asList(
                new double[] { 0.0, 0.0 },
                new double[] { 1.0, 0.0 },
                new double[] { 1.0, 1.0 },
                new double[] { 0.0, 1.0 }
        );

        // Create a list of edges
        List<int[]> edges = Arrays.asList(
                new int[] { 0, 1 },
                new int[] { 1, 2 },
                new int[] { 2, 3 },
                new int[] { 3, 0 }
        );

        // Create a list of faces
        List<int[]> faces = Arrays.asList(
                new int[] { 0, 1, 2 },
                new int[] { 2, 3, 0 }
        );

        // Mesh the points, edges, and faces
        meshing.mesh(points, edges, faces);

        // Get the mesh vertices
        double[][] vertices = meshing.getVertices();

        // Check that the mesh vertices are correct
        assertEquals(4, vertices.length);
        assertTrue(Math.abs(vertices[0][0] - 0.0) < EPS);
        assertTrue(Math.abs(vertices[0][1] - 0.0) < EPS);
        assertTrue(Math.abs(vertices[1][0] - 1.0) < EPS);
        assertTrue(Math.abs(vertices[1][1] - 0.0) < EPS);
        assertTrue(Math.abs(vertices[2][0] - 1.0) < EPS);
        assertTrue(Math.abs(vertices[2][1] - 1.0) < EPS);
        assertTrue(Math.abs(vertices[3][0] - 0.0) < EPS);
        assertTrue(Math.abs(vertices[3][1] - 1.0) < EPS);

        // Get the mesh edges
        int[][] edges2 = meshing.getEdges();

        // Check that the mesh edges are correct
        assertEquals(4, edges2.length);
        assertTrue(Arrays.equals(edges2[0], new int[] { 0, 1 }));
        assertTrue(Arrays.equals(edges2[1], new int[] { 1, 2 }));
        assertTrue(Arrays.equals(edges2[2], new int[] { 2, 3 }));
        assertTrue(Arrays.equals(edges2[3], new int[] { 3, 0 }));

        // Get the mesh faces
        int[][] faces2 = meshing.getFaces();

        // Check that the mesh faces are correct
        assertEquals(2, faces2.length);
        assertTrue(Arrays.equals(faces2[0], new int[] { 0, 1, 2 }));
        assertTrue(Arrays.equals(faces2[1], new int[] { 2, 3, 0 }));
    }
}
```