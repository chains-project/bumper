```java
import processing.core.PShape;

public class PGS_MorphologyGroupShapeTests {

  public void testGroupShape() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape group = new PShape();
    group.addChild(shape);

    PShape result = group.groupShape();

    assertEquals(shape, result);
  }

}
```