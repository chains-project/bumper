```java
import com.jcabi.aspects.Tv;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MkGithubTest {

    @Test
    public void testCreateRepo() {
        Tv tv = new Tv();
        assertEquals("1234567890", tv.get());
    }
}
```