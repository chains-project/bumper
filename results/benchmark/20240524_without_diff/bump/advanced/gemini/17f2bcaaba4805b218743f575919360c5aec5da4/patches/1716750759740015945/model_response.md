```java
import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class PGS_ProcessingGroupShapeTests {

  @Mock
  private PGS_ProcessingGroupShape pgs_ProcessingGroupShape;

  @Test
  public void testPgs_ProcessingGroupShape() {
    assertNotNull(pgs_ProcessingGroupShape);
  }
}
```