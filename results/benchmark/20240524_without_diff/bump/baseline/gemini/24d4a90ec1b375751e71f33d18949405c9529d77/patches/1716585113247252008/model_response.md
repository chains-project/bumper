```java
import com.jcabi.aspects.Tv;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;

public class BucketRuleTest {

    @Test
    public void test() {
        Tv tv = mock(Tv.class);
        assertEquals("tv", tv.toString());
    }
}
```