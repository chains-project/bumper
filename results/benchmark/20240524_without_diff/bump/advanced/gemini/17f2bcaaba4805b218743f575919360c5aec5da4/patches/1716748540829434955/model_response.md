```java
import org.junit.Assert;

public class PGS_MeshingTests {

    @org.junit.Test
    public void test_meshing_2D_with_holes_and_islands() {
        // Given
        List<Point> boundaryPoints = new ArrayList<>();
        boundaryPoints.add(new Point(0, 0));
        boundaryPoints.add(new Point(10, 0));
        boundaryPoints.add(new Point(10, 10));
        boundaryPoints.add(new Point(0, 10));

        List<Point> holePoints = new ArrayList<>();
        holePoints.add(new Point(2, 2));
        holePoints.add(new Point(8, 2));
        holePoints.add(new Point(8, 8));
        holePoints.add(new Point(2, 8));

        List<Point> islandPoints = new ArrayList<>();
        islandPoints.add(new Point(4, 4));
        islandPoints.add(new Point(6, 4));
        islandPoints.add(new Point(6, 6));
        islandPoints.add(new Point(4, 6));

        // When
        Mesh mesh = PGS.meshing(boundaryPoints, holePoints, islandPoints);

        // Then
        Assert.assertEquals(4, mesh.getTriangles().size());
        Assert.assertEquals(16, mesh.getVertices().size());
    }

    @org.junit.Test
    public void test_meshing_3D_with_holes_and_islands() {
        // Given
        List<Point> boundaryPoints = new ArrayList<>();
        boundaryPoints.add(new Point(0, 0, 0));
        boundaryPoints.add(new Point(10, 0, 0));
        boundaryPoints.add(new Point(10, 10, 0));
        boundaryPoints.add(new Point(0, 10, 0));
        boundaryPoints.add(new Point(0, 0, 10));
        boundaryPoints.add(new Point(10, 0, 10));
        boundaryPoints.add(new Point(10, 10, 10));
        boundaryPoints.add(new Point(0, 10, 10));

        List<Point> holePoints = new ArrayList<>();
        holePoints.add(new Point(2, 2, 2));
        holePoints.add(new Point(8, 2, 2));
        holePoints.add(new Point(8, 8, 2));
        holePoints.add(new Point(2, 8, 2));
        holePoints.add(new Point(2, 2, 8));
        holePoints.add(new Point(8, 2, 8));
        holePoints.add(new Point(8, 8, 8));
        holePoints.add(new Point(2, 8, 8));

        List<Point> islandPoints = new ArrayList<>();
        islandPoints.add(new Point(4, 4, 4));
        islandPoints.add(new Point(6, 4, 4));
        islandPoints.add(new Point(6, 6, 4));
        islandPoints.add(new Point(4, 6, 4));
        islandPoints.add(new Point(4, 4, 6));
        islandPoints.add(new Point(6, 4, 6));
        islandPoints.add(new Point(6, 6, 6));
        islandPoints.add(new Point(4, 6, 6));

        // When
        Mesh mesh = PGS.meshing(boundaryPoints, holePoints, islandPoints);

        // Then
        Assert.assertEquals(8, mesh.getTriangles().size());
        Assert.assertEquals(24, mesh.getVertices().size());
    }
}
```