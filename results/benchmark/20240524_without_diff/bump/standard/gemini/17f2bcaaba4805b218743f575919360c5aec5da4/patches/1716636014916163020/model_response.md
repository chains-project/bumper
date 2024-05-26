```java
import processing.core.PConstants;
import processing.core.PImage;

public class PGS_MorphologyGroupShapeTests {

  public void testGroupShape() {
    PImage img = new PImage(100, 100);
    img.loadPixels();
    for (int i = 0; i < img.pixels.length; i++) {
      img.pixels[i] = PConstants.WHITE;
    }
    img.updatePixels();

    // Create a group shape with a single rectangle
    PGS_GroupShape groupShape = new PGS_GroupShape();
    PGS_Rectangle rect = new PGS_Rectangle(10, 10, 20, 20);
    groupShape.addShape(rect);

    // Apply the group shape to the image
    PGS_Morphology.groupShape(img, groupShape, PConstants.MORPH_DILATE, 1);

    // Check that the pixels inside the rectangle are set to black
    for (int i = 10; i < 30; i++) {
      for (int j = 10; j < 30; j++) {
        assertEquals(PConstants.BLACK, img.pixels[i * img.width + j]);
      }
    }
  }
}
```