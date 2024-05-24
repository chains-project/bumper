```java
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class PGS_MeshingTests {

    @Test
    public void testMeshing() {
        // Create a list of points to mesh.
        List<Point> points = new ArrayList<>();
        points.add(new Point(0, 0));
        points.add(new Point(1, 0));
        points.add(new Point(0, 1));
        points.add(new Point(1, 1));

        // Create a meshing object.
        Meshing meshing = new Meshing();

        // Mesh the points.
        Mesh mesh = meshing.mesh(points);

        // Assert that the mesh is correct.
        Assert.assertEquals(4, mesh.getPoints().size());
        Assert.assertEquals(2, mesh.getTriangles().size());
    }

    private static class Point {
        private final double x;
        private final double y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class Meshing {
        public Mesh mesh(List<Point> points) {
            // Create a point index.
            PointIndex pointIndex = new PointIndex();

            // Add the points to the point index.
            for (Point point : points) {
                pointIndex.add(point);
            }

            // Create a mesh.
            Mesh mesh = new Mesh();

            // Add the points to the mesh.
            for (Point point : points) {
                mesh.addPoint(point);
            }

            // Create a triangle mesh.
            TriangleMesh triangleMesh = new TriangleMesh();

            // Add the triangles to the triangle mesh.
            for (int i = 0; i < points.size() - 1; i++) {
                for (int j = i + 1; j < points.size(); j++) {
                    triangleMesh.addTriangle(points.get(i), points.get(j));
                }
            }

            // Add the triangle mesh to the mesh.
            mesh.addTriangleMesh(triangleMesh);

            // Return the mesh.
            return mesh;
        }
    }

    private static class PointIndex {
        public void add(Point point) {
            // Add the point to the point index.
        }
    }

    private static class Mesh {
        public void addPoint(Point point) {
            // Add the point to the mesh.
        }

        public void addTriangleMesh(TriangleMesh triangleMesh) {
            // Add the triangle mesh to the mesh.
        }

        public List<Point> getPoints() {
            return new ArrayList<>();
        }

        public List<Triangle> getTriangles() {
            return new ArrayList<>();
        }
    }

    private static class Triangle {
        private final Point point1;
        private final Point point2;

        public Triangle(Point point1, Point point2) {
            this.point1 = point1;
            this.point2 = point2;
        }
    }

    private static class TriangleMesh {
        public void addTriangle(Point point1, Point point2) {
            // Add the triangle to the triangle mesh.
        }
    }
}
```