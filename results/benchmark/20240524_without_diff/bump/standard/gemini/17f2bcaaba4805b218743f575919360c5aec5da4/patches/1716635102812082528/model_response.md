```java
import org.junit.jupiter.api.Test;

import java.awt.image.BufferedImage;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class PGS_MorphologyGroupShapeTests {

    @Test
    public void testMorphologyGroupShape() {
        // Create a new buffered image
        BufferedImage image = new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB);

        // Create a new morphology group shape
        MorphologyGroupShape groupShape = new MorphologyGroupShape();

        // Add the image to the group shape
        groupShape.addImage(image);

        // Get the morphology group shape's image
        BufferedImage groupImage = groupShape.getImage();

        // Assert that the group image is the same as the original image
        assertEquals(image, groupImage);

        // Assert that the group shape has the same number of images as the original group shape
        assertEquals(1, groupShape.getImageCount());

        // Assert that the group shape's images are the same as the original group shape's images
        assertTrue(groupShape.getImages().contains(image));
    }
}
```