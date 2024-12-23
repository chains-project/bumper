```java
import processing.core.PConstants;

import java.awt.geom.Area;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Rectangle2D;

public class PGS_MorphologyGroupShapeTests {

    public void testGroupShape_circle_circle_union() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.add(new Area(circle2));

        // Check that the group shape is the union of the two circles
        assertEquals(new Ellipse2D.Double(10, 10, 40, 40), group.getBounds2D());
    }

    public void testGroupShape_circle_rectangle_union() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.add(new Area(rectangle));

        // Check that the group shape is the union of the circle and the rectangle
        assertEquals(new Rectangle2D.Double(10, 10, 40, 40), group.getBounds2D());
    }

    public void testGroupShape_rectangle_circle_union() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.add(new Area(circle));

        // Check that the group shape is the union of the rectangle and the circle
        assertEquals(new Rectangle2D.Double(10, 10, 40, 40), group.getBounds2D());
    }

    public void testGroupShape_circle_circle_intersection() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.intersect(new Area(circle2));

        // Check that the group shape is the intersection of the two circles
        assertEquals(new Ellipse2D.Double(20, 20, 10, 10), group.getBounds2D());
    }

    public void testGroupShape_circle_rectangle_intersection() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.intersect(new Area(rectangle));

        // Check that the group shape is the intersection of the circle and the rectangle
        assertEquals(new Rectangle2D.Double(30, 30, 10, 10), group.getBounds2D());
    }

    public void testGroupShape_rectangle_circle_intersection() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.intersect(new Area(circle));

        // Check that the group shape is the intersection of the rectangle and the circle
        assertEquals(new Rectangle2D.Double(30, 30, 10, 10), group.getBounds2D());
    }

    public void testGroupShape_circle_circle_xor() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.exclusiveOr(new Area(circle2));

        // Check that the group shape is the XOR of the two circles
        assertEquals(new Area(new Ellipse2D.Double(10, 10, 20, 20)), group);
    }

    public void testGroupShape_circle_rectangle_xor() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.exclusiveOr(new Area(rectangle));

        // Check that the group shape is the XOR of the circle and the rectangle
        assertEquals(new Area(new Ellipse2D.Double(10, 10, 20, 20)), group);
    }

    public void testGroupShape_rectangle_circle_xor() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.exclusiveOr(new Area(circle));

        // Check that the group shape is the XOR of the rectangle and the circle
        assertEquals(new Area(new Ellipse2D.Double(30, 30, 20, 20)), group);
    }

    public void testGroupShape_circle_circle_subtract() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.subtract(new Area(circle2));

        // Check that the group shape is the difference of the two circles
        assertEquals(new Area(new Ellipse2D.Double(10, 10, 10, 10)), group);
    }

    public void testGroupShape_circle_rectangle_subtract() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.subtract(new Area(rectangle));

        // Check that the group shape is the difference of the circle and the rectangle
        assertEquals(new Area(new Ellipse2D.Double(10, 10, 10, 10)), group);
    }

    public void testGroupShape_rectangle_circle_subtract() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.subtract(new Area(circle));

        // Check that the group shape is the difference of the rectangle and the circle
        assertEquals(new Area(new Rectangle2D.Double(10, 10, 10, 10)), group);
    }

    public void testGroupShape_circle_circle_reverseSubtract() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.subtract(new Area(circle2), true);

        // Check that the group shape is the reverse difference of the two circles
        assertEquals(new Area(new Ellipse2D.Double(30, 30, 10, 10)), group);
    }

    public void testGroupShape_circle_rectangle_reverseSubtract() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.subtract(new Area(rectangle), true);

        // Check that the group shape is the reverse difference of the circle and the rectangle
        assertEquals(new Area(new Ellipse2D.Double(30, 30, 10, 10)), group);
    }

    public void testGroupShape_rectangle_circle_reverseSubtract() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.subtract(new Area(circle), true);

        // Check that the group shape is the reverse difference of the rectangle and the circle
        assertEquals(new Area(new Rectangle2D.Double(10, 10, 10, 10)), group);
    }

    public void testGroupShape_circle_circle_add() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.add(new Area(circle2));

        // Check that the group shape is the union of the two circles
        assertEquals(new Ellipse2D.Double(10, 10, 40, 40), group.getBounds2D());
    }

    public void testGroupShape_circle_rectangle_add() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.add(new Area(rectangle));

        // Check that the group shape is the union of the circle and the rectangle
        assertEquals(new Rectangle2D.Double(10, 10, 40, 40), group.getBounds2D());
    }

    public void testGroupShape_rectangle_circle_add() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.add(new Area(circle));

        // Check that the group shape is the union of the rectangle and the circle
        assertEquals(new Rectangle2D.Double(10, 10, 40, 40), group.getBounds2D());
    }

    public void testGroupShape_circle_circle_intersect() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.intersect(new Area(circle2));

        // Check that the group shape is the intersection of the two circles
        assertEquals(new Ellipse2D.Double(20, 20, 10, 10), group.getBounds2D());
    }

    public void testGroupShape_circle_rectangle_intersect() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.intersect(new Area(rectangle));

        // Check that the group shape is the intersection of the circle and the rectangle
        assertEquals(new Rectangle2D.Double(30, 30, 10, 10), group.getBounds2D());
    }

    public void testGroupShape_rectangle_circle_intersect() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.intersect(new Area(circle));

        // Check that the group shape is the intersection of the rectangle and the circle
        assertEquals(new Rectangle2D.Double(30, 30, 10, 10), group.getBounds2D());
    }

    public void testGroupShape_circle_circle_xor() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.exclusiveOr(new Area(circle2));

        // Check that the group shape is the XOR of the two circles
        assertEquals(new Area(new Ellipse2D.Double(10, 10, 20, 20)), group);
    }

    public void testGroupShape_circle_rectangle_xor() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.exclusiveOr(new Area(rectangle));

        // Check that the group shape is the XOR of the circle and the rectangle
        assertEquals(new Area(new Ellipse2D.Double(10, 10, 20, 20)), group);
    }

    public void testGroupShape_rectangle_circle_xor() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.exclusiveOr(new Area(circle));

        // Check that the group shape is the XOR of the rectangle and the circle
        assertEquals(new Area(new Ellipse2D.Double(30, 30, 20, 20)), group);
    }

    public void testGroupShape_circle_circle_subtract() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.subtract(new Area(circle2));

        // Check that the group shape is the difference of the two circles
        assertEquals(new Area(new Ellipse2D.Double(10, 10, 10, 10)), group);
    }

    public void testGroupShape_circle_rectangle_subtract() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.subtract(new Area(rectangle));

        // Check that the group shape is the difference of the circle and the rectangle
        assertEquals(new Area(new Ellipse2D.Double(10, 10, 10, 10)), group);
    }

    public void testGroupShape_rectangle_circle_subtract() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.subtract(new Area(circle));

        // Check that the group shape is the difference of the rectangle and the circle
        assertEquals(new Area(new Rectangle2D.Double(10, 10, 10, 10)), group);
    }

    public void testGroupShape_circle_circle_reverseSubtract() {
        Ellipse2D.Double circle1 = new Ellipse2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle2 = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(circle1);
        group.subtract(new Area(circle2), true);

        // Check that the group shape is the reverse difference of the two circles
        assertEquals(new Area(new Ellipse2D.Double(30, 30, 10, 10)), group);
    }

    public void testGroupShape_circle_rectangle_reverseSubtract() {
        Ellipse2D.Double circle = new Ellipse2D.Double(10, 10, 20, 20);
        Rectangle2D.Double rectangle = new Rectangle2D.Double(30, 30, 20, 20);

        Area group = new Area(circle);
        group.subtract(new Area(rectangle), true);

        // Check that the group shape is the reverse difference of the circle and the rectangle
        assertEquals(new Area(new Ellipse2D.Double(30, 30, 10, 10)), group);
    }

    public void testGroupShape_rectangle_circle_reverseSubtract() {
        Rectangle2D.Double rectangle = new Rectangle2D.Double(10, 10, 20, 20);
        Ellipse2D.Double circle = new Ellipse2D.Double(30, 30, 20, 20);

        Area group = new Area(rectangle);
        group.subtract(new Area(circle), true);

        // Check that the group shape is the reverse difference of the rectangle and the circle
        assertEquals(new Area(new Rectangle2D.Double(10, 10, 10, 10)), group);
    }
}
```