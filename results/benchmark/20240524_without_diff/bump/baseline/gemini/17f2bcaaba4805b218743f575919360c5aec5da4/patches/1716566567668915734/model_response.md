```java
import static org.junit.Assume.assumeTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

import micycle.pgs.PGS_MorphologyGroupShape;
import micycle.pgs.PGS_MorphologyGroupShape.Shape;
import micycle.pgs.PGS_MorphologyGroupShape.Shape.Point;
import micycle.pgs.PGS_MorphologyGroupShape.Shape.Polygon;
import micycle.pgs.PGS_MorphologyGroupShape.Shape.Polyline;

public class PGS_MorphologyGroupShapeTests {

  @Test
  public void testGroupShape() {
    // Create a group shape with two shapes.
    List<Shape> shapes = new ArrayList<>();
    shapes.add(new Polygon(new Point(0, 0), new Point(10, 0), new Point(10, 10), new Point(0, 10)));
    shapes.add(new Polyline(new Point(5, 5), new Point(5, 15), new Point(15, 15)));
    PGS_MorphologyGroupShape groupShape = new PGS_MorphologyGroupShape(shapes);

    // Assume that the group shape is not empty.
    assumeTrue(!groupShape.isEmpty());

    // Check that the group shape contains the two shapes.
    assert groupShape.getShapes().size() == 2;
    assert groupShape.getShapes().contains(shapes.get(0));
    assert groupShape.getShapes().contains(shapes.get(1));

    // Check that the group shape has the correct bounding box.
    assert groupShape.getBoundingBox().getMinX() == 0;
    assert groupShape.getBoundingBox().getMinY() == 0;
    assert groupShape.getBoundingBox().getMaxX() == 15;
    assert groupShape.getBoundingBox().getMaxY() == 15;
  }
}
```