```java
  import com.jcabi.aspects.Tv;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class RegionITCase {

    @Test
    public void testRegion() {
        // Arrange
        Tv tv = new Tv();
        // Act
        tv.on();
        // Assert
        assertEquals("on", tv.getState());
    }
}
```