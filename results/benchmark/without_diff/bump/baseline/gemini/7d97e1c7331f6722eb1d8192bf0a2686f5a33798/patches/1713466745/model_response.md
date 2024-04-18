```java
  import com.jcabi.aspects.Tv;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class RegionITCase {

    @Test
    void testRegion() {
        assertEquals("us-east-1", new Tv().region());
    }
}
```