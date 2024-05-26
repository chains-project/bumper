```java
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {

    @org.junit.jupiter.api.Test
    public void testMorphologyGroupShape() throws Exception {
        // Arrange
        PGS pgs = new PGS();
        pgs.setVerbose(true);
        pgs.setDebug(true);

        // Act
        String result = pgs.execute("morphologyGroupShape", "1");

        // Assert
        assertEquals("1", result);
    }
}
```