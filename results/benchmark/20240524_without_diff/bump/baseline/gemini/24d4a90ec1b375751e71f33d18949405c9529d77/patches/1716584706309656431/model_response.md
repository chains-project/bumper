```java
import com.jcabi.aspects.Tv;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class AwsOcketITCase {

  private final Tv tv = new Tv();

  @Test
  void testAwsOcket() {
    assertTrue(tv.play("http://example.com"));
    assertFalse(tv.play("http://example.com"));
  }
}
```