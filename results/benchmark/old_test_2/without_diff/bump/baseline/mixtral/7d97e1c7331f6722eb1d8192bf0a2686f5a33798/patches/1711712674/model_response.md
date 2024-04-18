Here is a fixed version of the failing method that removes the dependency on the problematic library:

```java
import org.junit.Test;
import java.io.IOException;
import java.util.Arrays;
import java.util.stream.Collectors;

@Test
public class RegionITCase {
    @Test
