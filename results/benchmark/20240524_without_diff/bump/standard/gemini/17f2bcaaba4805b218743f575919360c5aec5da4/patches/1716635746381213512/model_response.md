```java
import processing.core.PConstants;
import processing.core.PApplet;

public class PGS_MorphologyGroupShapeTests extends PApplet {

  public void setup() {
    size(500, 500);
    background(255);
    noLoop();
  }

  public void draw() {
    // Create a PShape object
    PShape shape = createShape(GROUP);

    // Add a rectangle to the shape
    shape.beginShape();
    shape.vertex(100, 100);
    shape.vertex(200, 100);
    shape.vertex(200, 200);
    shape.vertex(100, 200);
    shape.endShape(CLOSE);

    // Create a PShape object for the outline
    PShape outline = shape.getOutline();

    // Set the stroke weight
    strokeWeight(5);

    // Draw the outline
    stroke(0);
    shape(outline);

    // Draw the shape
    fill(255, 0, 0);
    shape(shape);
  }

  public static void main(String[] args) {
    PApplet.main(PGS_MorphologyGroupShapeTests.class.getName());
  }
}
```