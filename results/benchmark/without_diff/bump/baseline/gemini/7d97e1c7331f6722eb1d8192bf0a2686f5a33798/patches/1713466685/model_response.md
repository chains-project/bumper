```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.Tv.On;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertNotNull;

@On("http://localhost:8080")
public class RegionITCase {

  @Test
  void testRegion() {
    final Tv tv = new Tv();
    assertNotNull(tv.region());
  }
}
```