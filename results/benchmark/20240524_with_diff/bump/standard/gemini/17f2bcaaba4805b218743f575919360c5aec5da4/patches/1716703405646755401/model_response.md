```java
import static org.junit.Assume.assumeThat;

public class PGS_ProcessingGroupShapeTests {

    @Test
    public void testProcessingGroupShapes() {
        assumeThat(System.getProperty("os.name"), not(containsString("Windows")));
        // ...
    }

    @Test
    public void testProcessingGroupShapes_Windows() {
        assumeThat(System.getProperty("os.name"), containsString("Windows"));
        // ...
    }
}
```