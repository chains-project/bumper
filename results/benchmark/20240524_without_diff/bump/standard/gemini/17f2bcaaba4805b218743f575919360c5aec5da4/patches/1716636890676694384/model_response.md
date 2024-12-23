```java
import processing.core.PShape;
import processing.core.PVector;

public class PGS_MorphologyGroupShapeTests {

  public void testGroup() {
    PShape shape1 = new PShape();
    shape1.beginShape();
    shape1.vertex(0, 0);
    shape1.vertex(10, 0);
    shape1.vertex(10, 10);
    shape1.vertex(0, 10);
    shape1.endShape();

    PShape shape2 = new PShape();
    shape2.beginShape();
    shape2.vertex(5, 5);
    shape2.vertex(15, 5);
    shape2.vertex(15, 15);
    shape2.vertex(5, 15);
    shape2.endShape();

    PShape[] shapes = {shape1, shape2};
    PShape group = new PShape(PShape.GROUP);
    group.addChild(shape1);
    group.addChild(shape2);

    PVector offset = new PVector(10, 10);
    group.translate(offset.x, offset.y);

    PShape result = group.getTransformedPShape();

    assertEquals(2, result.getChildCount());
    assertEquals(shape1.getVertexCount(), result.getChild(0).getVertexCount());
    assertEquals(shape2.getVertexCount(), result.getChild(1).getVertexCount());
    for (int i = 0; i < shape1.getVertexCount(); i++) {
      PVector v1 = shape1.getVertex(i);
      PVector v2 = result.getChild(0).getVertex(i);
      assertEquals(v1.x + offset.x, v2.x, 0.001);
      assertEquals(v1.y + offset.y, v2.y, 0.001);
    }
    for (int i = 0; i < shape2.getVertexCount(); i++) {
      PVector v1 = shape2.getVertex(i);
      PVector v2 = result.getChild(1).getVertex(i);
      assertEquals(v1.x + offset.x, v2.x, 0.001);
      assertEquals(v1.y + offset.y, v2.y, 0.001);
    }
  }
}
```