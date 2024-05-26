```java
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

public class PGS_ProcessingGroupShapeTests {

    @Test
    public void testAssumeTrue() {
        assertThrows(IllegalStateException.class, () -> assumeTrue(false, "This should fail"));
    }
}
```