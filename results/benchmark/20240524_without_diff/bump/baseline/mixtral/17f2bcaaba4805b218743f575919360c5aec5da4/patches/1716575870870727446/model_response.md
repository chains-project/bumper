Here's the proposed patch:
```java
import org.junit.Assert.*;
import org.junit.Test;

public class PGS_MorphologyGroupShapeTests {
    // existing code...

    @Test
    public void testMorphologyGroupShape() {
        assumeTrue(/* your condition here */);
        // rest of the method...
    }
}
```
Replace the `import static org.junit.Assume.assumeTrue;` line with the above code.

The patch replaces the static import with an import for the Assert class and uses a regular method call to `assumeTrue()`.

Confidence: 90%