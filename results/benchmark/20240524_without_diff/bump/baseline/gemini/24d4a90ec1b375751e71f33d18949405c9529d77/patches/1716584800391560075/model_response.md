```java
import com.jcabi.aspects.Tv;
import org.junit.jupiter.api.Test;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class AwsOcketITCase {

    @Test
    public void test() {
        Tv tv = mock(Tv.class);
        when(tv.name()).thenReturn("name");
        when(tv.model()).thenReturn("model");
        when(tv.year()).thenReturn(2023);
        when(tv.isSmart()).thenReturn(true);
        when(tv.is3D()).thenReturn(false);
        when(tv.is4K()).thenReturn(true);
    }
}
```