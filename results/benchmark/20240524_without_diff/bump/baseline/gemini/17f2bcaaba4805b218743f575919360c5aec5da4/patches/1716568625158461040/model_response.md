```java
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.List;

public class FastPolygonizerTests {

    @Ignore
    public void testPolygonize_with_hole_and_multiple_holes() {
        List<Point> points = new ArrayList<>();
        points.add(new Point(0, 0));
        points.add(new Point(10, 0));
        points.add(new Point(10, 10));
        points.add(new Point(0, 10));
        points.add(new Point(5, 5));
        points.add(new Point(5, 6));
        points.add(new Point(6, 6));
        points.add(new Point(6, 5));

        List<List<Point>> expectedHoles = new ArrayList<>();
        List<Point> hole1 = new ArrayList<>();
        hole1.add(new Point(2, 2));
        hole1.add(new Point(8, 2));
        hole1.add(new Point(8, 8));
        hole1.add(new Point(2, 8));
        expectedHoles.add(hole1);

        List<Point> hole2 = new ArrayList<>();
        hole2.add(new Point(3, 3));
        hole2.add(new Point(7, 3));
        hole2.add(new Point(7, 7));
        hole2.add(new Point(3, 7));
        expectedHoles.add(hole2);

        List<List<Point>> result = FastPolygonizer.polygonize(points, expectedHoles);

        assertEquals(1, result.size());
        List<Point> polygon = result.get(0);
        assertEquals(9, polygon.size());
        assertEquals(new Point(0, 0), polygon.get(0));
        assertEquals(new Point(10, 0), polygon.get(1));
        assertEquals(new Point(10, 10), polygon.get(2));
        assertEquals(new Point(0, 10), polygon.get(3));
        assertEquals(new Point(5, 5), polygon.get(4));
        assertEquals(new Point(5, 6), polygon.get(5));
        assertEquals(new Point(6, 6), polygon.get(6));
        assertEquals(new Point(6, 5), polygon.get(7));
        assertEquals(new Point(0, 0), polygon.get(8));

        List<List<Point>> holes = result.subList(1, result.size());
        assertEquals(2, holes.size());

        List<Point> hole = holes.get(0);
        assertEquals(5, hole.size());
        assertEquals(new Point(2, 2), hole.get(0));
        assertEquals(new Point(8, 2), hole.get(1));
        assertEquals(new Point(8, 8), hole.get(2));
        assertEquals(new Point(2, 8), hole.get(3));
        assertEquals(new Point(2, 2), hole.get(4));

        hole = holes.get(1);
        assertEquals(5, hole.size());
        assertEquals(new Point(3, 3), hole.get(0));
        assertEquals(new Point(7, 3), hole.get(1));
        assertEquals(new Point(7, 7), hole.get(2));
        assertEquals(new Point(3, 7), hole.get(3));
        assertEquals(new Point(3, 3), hole.get(4));
    }

    @Ignore
    public void testPolygonize_with_hole_and_multiple_holes_and_zero_area_holes() {
        List<Point> points = new ArrayList<>();
        points.add(new Point(0, 0));
        points.add(new Point(10, 0));
        points.add(new Point(10, 10));
        points.add(new Point(0, 10));
        points.add(new Point(5, 5));
        points.add(new Point(5, 6));
        points.add(new Point(6, 6));
        points.add(new Point(6, 5));

        List<List<Point>> expectedHoles = new ArrayList<>();
        List<Point> hole1 = new ArrayList<>();
        hole1.add(new Point(2, 2));
        hole1.add(new Point(8, 2));
        hole1.add(new Point(8, 8));
        hole1.add(new Point(2, 8));
        expectedHoles.add(hole1);

        List<Point> hole2 = new ArrayList<>();
        hole2.add(new Point(3, 3));
        hole2.add(new Point(7, 3));
        hole2.add(new Point(7, 7));
        hole2.add(new Point(3, 7));
        expectedHoles.add(hole2);

        List<Point> hole3 = new ArrayList<>();
        hole3.add(new Point(4, 4));
        hole3.add(new Point(6, 4));
        hole3.add(new Point(6, 6));
        hole3.add(new Point(4, 6));
        expectedHoles.add(hole3);

        List<List<Point>> result = FastPolygonizer.polygonize(points, expectedHoles);

        assertEquals(1, result.size());
        List<Point> polygon = result.get(0);
        assertEquals(9, polygon.size());
        assertEquals(new Point(0, 0), polygon.get(0));
        assertEquals(new Point(10, 0), polygon.get(1));
        assertEquals(new Point(10, 10), polygon.get(2));
        assertEquals(new Point(0, 10), polygon.get(3));
        assertEquals(new Point(5, 5), polygon.get(4));
        assertEquals(new Point(5, 6), polygon.get(5));
        assertEquals(new Point(6, 6), polygon.get(6));
        assertEquals(new Point(6, 5), polygon.get(7));
        assertEquals(new Point(0, 0), polygon.get(8));

        List<List<Point>> holes = result.subList(1, result.size());
        assertEquals(2, holes.size());

        List<Point> hole = holes.get(0);
        assertEquals(5, hole.size());
        assertEquals(new Point(2, 2), hole.get(0));
        assertEquals(new Point(8, 2), hole.get(1));
        assertEquals(new Point(8, 8), hole.get(2));
        assertEquals(new Point(2, 8), hole.get(3));
        assertEquals(new Point(2, 2), hole.get(4));

        hole = holes.get(1);
        assertEquals(5, hole.size());
        assertEquals(new Point(3, 3), hole.get(0));
        assertEquals(new Point(7, 3), hole.get(1));
        assertEquals(new Point(7, 7), hole.get(2));
        assertEquals(new Point(3, 7), hole.get(3));
        assertEquals(new Point(3, 3), hole.get(4));
    }

    @Ignore
    public void testPolygonize_with_hole_and_multiple_holes_and_zero_area_holes_and_collinear_points() {
        List<Point> points = new ArrayList<>();
        points.add(new Point(0, 0));
        points.add(new Point(10, 0));
        points.add(new Point(10, 10));
        points.add(new Point(0, 10));
        points.add(new Point(5, 5));
        points.add(new Point(5, 6));
        points.add(new Point(6, 6));
        points.add(new Point(6, 5));

        List<List<Point>> expectedHoles = new ArrayList<>();
        List<Point> hole1 = new ArrayList<>();
        hole1.add(new Point(2, 2));
        hole1.add(new Point(8, 2));
        hole1.add(new Point(8, 8));
        hole1.add(new Point(2, 8));
        expectedHoles.add(hole1);

        List<Point> hole2 = new ArrayList<>();
        hole2.add(new Point(3, 3));
        hole2.add(new Point(7, 3));
        hole2.add(new Point(7, 7));
        hole2.add(new Point(3, 7));
        expectedHoles.add(hole2);

        List<Point> hole3 = new ArrayList<>();
        hole3.add(new Point(4, 4));
        hole3.add(new Point(6, 4));
        hole3.add(new Point(6, 6));
        hole3.add(new Point(4, 6));
        expectedHoles.add(hole3);

        List<Point> hole4 = new ArrayList<>();
        hole4.add(new Point(5, 5));
        hole4.add(new Point(5, 6));
        hole4.add(new Point(6, 6));
        hole4.add(new Point(6, 5));
        expectedHoles.add(hole4);

        List<List<Point>> result = FastPolygonizer.polygonize(points, expectedHoles);

        assertEquals(1, result.size());
        List<Point> polygon = result.get(0);
        assertEquals(9, polygon.size());
        assertEquals(new Point(0, 0), polygon.get(0));
        assertEquals(new Point(10, 0), polygon.get(1));
        assertEquals(new Point(10, 10), polygon.get(2));
        assertEquals(new Point(0, 10), polygon.get(3));
        assertEquals(new Point(5, 5), polygon.get(4));
        assertEquals(new Point(5, 6), polygon.get(5));
        assertEquals(new Point(6, 6), polygon.get(6));
        assertEquals(new Point(6, 5), polygon.get(7));
        assertEquals(new Point(0, 0), polygon.get(8));

        List<List<Point>> holes = result.subList(1, result.size());
        assertEquals(2, holes.size());

        List<Point> hole = holes.get(0);
        assertEquals(5, hole.size());
        assertEquals(new Point(2, 2), hole.get(0));
        assertEquals(new Point(8, 2), hole.get(1));
        assertEquals(new Point(8, 8), hole.get(2));
        assertEquals(new Point(2, 8), hole.get(3));
        assertEquals(new Point(2, 2), hole.get(4));

        hole = holes.get(1);
        assertEquals(5, hole.size());
        assertEquals(new Point(3, 3), hole.get(0));
        assertEquals(new Point(7, 3), hole.get(1));
        assertEquals(new Point(7, 7), hole.get(2));
        assertEquals(new Point(3, 7), hole.get(3));
        assertEquals(new Point(3, 3), hole.get(4));
    }

}
```