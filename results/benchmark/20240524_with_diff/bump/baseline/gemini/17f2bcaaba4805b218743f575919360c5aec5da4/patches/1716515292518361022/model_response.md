```java
import org.junit.Assume;

public class PGS_MorphologyGroupShapeTests {

    public void testMorphologyGroupShape(String fileName) throws Exception {
        assumeTrue(fileName.endsWith("png"));
        // ...
    }
}
```