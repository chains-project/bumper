```java
import static org.junit.Assume.assumeThat;

import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

public class PGS_ProcessingGroupShapeTests {

  @Test
  public void testProcessingGroupShape() {
    assumeThat("This test is only run on Linux", System.getProperty("os.name"),
        Matchers.equalToIgnoringCase("Linux"));
  }
}
```