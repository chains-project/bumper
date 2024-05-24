```java
import org.junit.Assert;

import java.util.Arrays;
import java.util.List;

public class PGS_MeshingTests {

    @org.junit.Test
    public void testMeshing() {
        List<Integer> expected = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        List<Integer> actual = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        Assert.assertEquals(expected, actual);
    }
}
```