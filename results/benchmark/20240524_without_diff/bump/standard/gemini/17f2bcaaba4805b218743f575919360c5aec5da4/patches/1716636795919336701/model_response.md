```java
import processing.core.PShape;
import processing.core.PVector;

public class PGS_MorphologyGroupShapeTests {

  public static void main(String[] args) {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape group = new PShape();
    group.addChild(shape);

    PShape dilated = group.dilate(5);

    // Test that the dilated shape is the correct size.
    PVector[] vertices = dilated.getVertices();
    assertEquals(4, vertices.length);
    assertEquals(new PVector(-5, -5), vertices[0]);
    assertEquals(new PVector(15, -5), vertices[1]);
    assertEquals(new PVector(15, 15), vertices[2]);
    assertEquals(new PVector(-5, 15), vertices[3]);
  }
}
```