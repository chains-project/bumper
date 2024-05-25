```java
import com.jcabi.aspects.Tv;
import org.junit.jupiter.api.Test;

import java.sql.SQLException;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class RegionITCase {

    @Test
    void testRegion() throws SQLException {
        Tv tv = mock(Tv.class);
        when(tv.name()).thenReturn("us-east-1");
        // TODO: Implement test
    }
}
```