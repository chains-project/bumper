```java
package micycle.pgs;
import org.junit.Assert;
import static org.junit.Assert.*;
public class PGS_MeshingTests {
    @org.junit.Test(timeout = 3600000)
    public void testMeshing_0_1_0() throws Exception {
        double[][] vertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] faces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedVertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] expectedFaces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedNormals = {
            {0.5773502691896258, -0.5773502691896258, 0.5773502691896258},
            {0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, 0.5773502691896258},
            {-0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
        };
        double[] expectedAreas = {
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        };
        double[] expectedVolumes = {
            0.125,
        };
        PGS_Mesh mesh = new PGS_Mesh(vertices, faces);
        mesh.computeNormals();
        mesh.computeAreas();
        mesh.computeVolumes();
        Assert.assertArrayEquals(expectedVertices, mesh.getVertices(), 1e-6);
        Assert.assertArrayEquals(expectedFaces, mesh.getFaces());
        Assert.assertArrayEquals(expectedNormals, mesh.getNormals(), 1e-6);
        Assert.assertArrayEquals(expectedAreas, mesh.getAreas(), 1e-6);
        Assert.assertArrayEquals(expectedVolumes, mesh.getVolumes(), 1e-6);
    }

    @org.junit.Test(timeout = 3600000)
    public void testMeshing_1_0_1() throws Exception {
        double[][] vertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] faces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedVertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] expectedFaces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedNormals = {
            {0.5773502691896258, -0.5773502691896258, 0.5773502691896258},
            {0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, 0.5773502691896258},
            {-0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
        };
        double[] expectedAreas = {
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        };
        double[] expectedVolumes = {
            0.125,
        };
        PGS_Mesh mesh = new PGS_Mesh(vertices, faces);
        mesh.computeNormals();
        mesh.computeAreas();
        mesh.computeVolumes();
        Assert.assertArrayEquals(expectedVertices, mesh.getVertices(), 1e-6);
        Assert.assertArrayEquals(expectedFaces, mesh.getFaces());
        Assert.assertArrayEquals(expectedNormals, mesh.getNormals(), 1e-6);
        Assert.assertArrayEquals(expectedAreas, mesh.getAreas(), 1e-6);
        Assert.assertArrayEquals(expectedVolumes, mesh.getVolumes(), 1e-6);
    }

    @org.junit.Test(timeout = 3600000)
    public void testMeshing_1_0_2() throws Exception {
        double[][] vertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] faces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedVertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] expectedFaces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedNormals = {
            {0.5773502691896258, -0.5773502691896258, 0.5773502691896258},
            {0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, 0.5773502691896258},
            {-0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
        };
        double[] expectedAreas = {
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        };
        double[] expectedVolumes = {
            0.125,
        };
        PGS_Mesh mesh = new PGS_Mesh(vertices, faces);
        mesh.computeNormals();
        mesh.computeAreas();
        mesh.computeVolumes();
        Assert.assertArrayEquals(expectedVertices, mesh.getVertices(), 1e-6);
        Assert.assertArrayEquals(expectedFaces, mesh.getFaces());
        Assert.assertArrayEquals(expectedNormals, mesh.getNormals(), 1e-6);
        Assert.assertArrayEquals(expectedAreas, mesh.getAreas(), 1e-6);
        Assert.assertArrayEquals(expectedVolumes, mesh.getVolumes(), 1e-6);
    }

    @org.junit.Test(timeout = 3600000)
    public void testMeshing_1_1_0() throws Exception {
        double[][] vertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] faces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedVertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] expectedFaces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedNormals = {
            {0.5773502691896258, -0.5773502691896258, 0.5773502691896258},
            {0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, 0.5773502691896258},
            {-0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
        };
        double[] expectedAreas = {
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        };
        double[] expectedVolumes = {
            0.125,
        };
        PGS_Mesh mesh = new PGS_Mesh(vertices, faces);
        mesh.computeNormals();
        mesh.computeAreas();
        mesh.computeVolumes();
        Assert.assertArrayEquals(expectedVertices, mesh.getVertices(), 1e-6);
        Assert.assertArrayEquals(expectedFaces, mesh.getFaces());
        Assert.assertArrayEquals(expectedNormals, mesh.getNormals(), 1e-6);
        Assert.assertArrayEquals(expectedAreas, mesh.getAreas(), 1e-6);
        Assert.assertArrayEquals(expectedVolumes, mesh.getVolumes(), 1e-6);
    }

    @org.junit.Test(timeout = 3600000)
    public void testMeshing_1_1_1() throws Exception {
        double[][] vertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] faces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedVertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] expectedFaces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedNormals = {
            {0.5773502691896258, -0.5773502691896258, 0.5773502691896258},
            {0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, 0.5773502691896258},
            {-0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
        };
        double[] expectedAreas = {
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        };
        double[] expectedVolumes = {
            0.125,
        };
        PGS_Mesh mesh = new PGS_Mesh(vertices, faces);
        mesh.computeNormals();
        mesh.computeAreas();
        mesh.computeVolumes();
        Assert.assertArrayEquals(expectedVertices, mesh.getVertices(), 1e-6);
        Assert.assertArrayEquals(expectedFaces, mesh.getFaces());
        Assert.assertArrayEquals(expectedNormals, mesh.getNormals(), 1e-6);
        Assert.assertArrayEquals(expectedAreas, mesh.getAreas(), 1e-6);
        Assert.assertArrayEquals(expectedVolumes, mesh.getVolumes(), 1e-6);
    }

    @org.junit.Test(timeout = 3600000)
    public void testMeshing_1_1_2() throws Exception {
        double[][] vertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] faces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedVertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] expectedFaces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedNormals = {
            {0.5773502691896258, -0.5773502691896258, 0.5773502691896258},
            {0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, 0.5773502691896258},
            {-0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
        };
        double[] expectedAreas = {
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        };
        double[] expectedVolumes = {
            0.125,
        };
        PGS_Mesh mesh = new PGS_Mesh(vertices, faces);
        mesh.computeNormals();
        mesh.computeAreas();
        mesh.computeVolumes();
        Assert.assertArrayEquals(expectedVertices, mesh.getVertices(), 1e-6);
        Assert.assertArrayEquals(expectedFaces, mesh.getFaces());
        Assert.assertArrayEquals(expectedNormals, mesh.getNormals(), 1e-6);
        Assert.assertArrayEquals(expectedAreas, mesh.getAreas(), 1e-6);
        Assert.assertArrayEquals(expectedVolumes, mesh.getVolumes(), 1e-6);
    }

    @org.junit.Test(timeout = 3600000)
    public void testMeshing_2_1_0() throws Exception {
        double[][] vertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] faces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedVertices = {
            {1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {0.0, 0.0, 1.0},
            {1.0, 1.0, 0.0},
            {1.0, 0.0, 1.0},
            {0.0, 1.0, 1.0},
        };
        int[][] expectedFaces = {
            {0, 1, 2},
            {0, 3, 4},
            {0, 5, 1},
            {1, 3, 5},
            {2, 4, 5},
            {3, 4, 2},
        };
        double[][] expectedNormals = {
            {0.5773502691896258, -0.5773502691896258, 0.5773502691896258},
            {0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, 0.5773502691896258},
            {-0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {0.5773502691896258, -0.5773502691896258, -0.5773502691896258},
            {-0.5773502691896258, 0.5773502691896258, -0.5773502691896258},
        };
        double[] expectedAreas = {
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        };
        double[] expectedVolumes = {
            0.125,
        };
        PGS_Mesh mesh = new PGS_Mesh(vertices, faces);
        mesh.computeNormals();
        mesh.computeAreas();
        mesh.computeVolumes();
        Assert.assertArrayEquals(expectedVertices, mesh.getVertices(), 1e-6);
        Assert.assertArrayEquals(expectedFaces, mesh.getFaces());
        Assert.assertArrayEquals(expectedNormals, mesh.getNormals(), 1e-6);
        Assert.assertArrayEquals(expectedAreas, mesh.getAreas(), 1e-6);
        Assert.assertArrayEquals(expectedVolumes, mesh.getVolumes(), 1e-6);
    }
}
```