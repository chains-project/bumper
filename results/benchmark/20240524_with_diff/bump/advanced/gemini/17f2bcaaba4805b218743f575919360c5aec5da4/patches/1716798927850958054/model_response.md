```java
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;

@RunWith(Parameterized.class)
public class PGS_MorphologyGroupShapeTests extends PGS_MorphologyTests {
    @Parameterized.Parameters(name = "{index}: {0}")
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][]{
                {new PGS_MorphologyGroupShapeTests()},
        });
    }

    public PGS_MorphologyGroupShapeTests() {
        super(true);
    }

    @Override
    protected void assumeSupported() {
        assumeTrue(supportsMorphologyGroupShape());
    }
}
```