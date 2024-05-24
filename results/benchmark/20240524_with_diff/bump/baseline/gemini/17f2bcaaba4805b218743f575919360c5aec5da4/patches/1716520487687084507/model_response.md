```java
import org.junit.Assert;

import java.util.List;

import static org.junit.Assert.assertTrue;

public class PGS_MeshingTests {

    @org.junit.Test
    public void testMeshing1() {
        PGS pgs = new PGS();
        List<Point> points = List.of(
                new Point(0, 0, 0),
                new Point(1, 0, 0),
                new Point(0, 1, 0),
                new Point(1, 1, 0),
                new Point(0, 0, 1),
                new Point(1, 0, 1),
                new Point(0, 1, 1),
                new Point(1, 1, 1)
        );
        PGSMesh mesh = pgs.generateMesh(points, 1);
        Assert.assertEquals(8, mesh.getVertices().size());
        Assert.assertEquals(12, mesh.getEdges().size());
        Assert.assertEquals(6, mesh.getFaces().size());
    }

    @org.junit.Test
    public void testMeshing2() {
        PGS pgs = new PGS();
        List<Point> points = List.of(
                new Point(0, 0, 0),
                new Point(1, 0, 0),
                new Point(0, 1, 0),
                new Point(1, 1, 0),
                new Point(0, 0, 1),
                new Point(1, 0, 1),
                new Point(0, 1, 1),
                new Point(1, 1, 1),
                new Point(0.5, 0.5, 0.5)
        );
        PGSMesh mesh = pgs.generateMesh(points, 1);
        Assert.assertEquals(9, mesh.getVertices().size());
        Assert.assertEquals(18, mesh.getEdges().size());
        Assert.assertEquals(12, mesh.getFaces().size());
    }

    @org.junit.Test
    public void testMeshing3() {
        PGS pgs = new PGS();
        List<Point> points = List.of(
                new Point(0, 0, 0),
                new Point(1, 0, 0),
                new Point(0, 1, 0),
                new Point(1, 1, 0),
                new Point(0, 0, 1),
                new Point(1, 0, 1),
                new Point(0, 1, 1),
                new Point(1, 1, 1),
                new Point(0.25, 0.25, 0.25),
                new Point(0.75, 0.25, 0.25),
                new Point(0.25, 0.75, 0.25),
                new Point(0.75, 0.75, 0.25),
                new Point(0.25, 0.25, 0.75),
                new Point(0.75, 0.25, 0.75),
                new Point(0.25, 0.75, 0.75),
                new Point(0.75, 0.75, 0.75)
        );
        PGSMesh mesh = pgs.generateMesh(points, 1);
        Assert.assertEquals(16, mesh.getVertices().size());
        Assert.assertEquals(48, mesh.getEdges().size());
        Assert.assertEquals(32, mesh.getFaces().size());
    }

    private static class Point {
        final double x;
        final double y;
        final double z;

        Point(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }
}
```