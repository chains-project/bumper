```java
import processing.core.PConstants;
import processing.core.PImage;

public class PGS_MorphologyGroupShapeTests extends PApplet {

  public void setup() {
    size(100, 100);
    noLoop();
  }

  public void draw() {
    PImage img = loadImage("test.png");
    img.filter(PConstants.INVERT);
    image(img, 0, 0);
  }

  public static void main(String[] args) {
    PApplet.main(new String[] { "--present", PGS_MorphologyGroupShapeTests.class.getName() });
  }
}
```