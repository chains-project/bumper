```java
import static org.junit.Assume.assumeThat;
import org.hamcrest.Matchers;

public class PGS_MorphologyGroupShapeTests {
    @Test
    public void test_PGS_MorphologyGroupShape_1() {
        assumeThat("Test only runs on Linux", SystemUtils.IS_OS_LINUX, Matchers.is(true));
        // ...
    }
}
```