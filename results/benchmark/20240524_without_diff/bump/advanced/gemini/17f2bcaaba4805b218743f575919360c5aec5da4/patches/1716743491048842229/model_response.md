```java
import static org.junit.Assume.assumeTrue;

public class PGS_MorphologyGroupShapeTests {

    @Test
    public void test_group_shape_basic() {
        assumeTrue(System.getProperty("os.name").contains("Linux"));
        // ...
    }

    @Test
    public void test_group_shape_basic_with_options() {
        assumeTrue(System.getProperty("os.name").contains("Linux"));
        // ...
    }

    @Test
    public void test_group_shape_with_options() {
        assumeTrue(System.getProperty("os.name").contains("Linux"));
        // ...
    }

    @Test
    public void test_group_shape_with_options_and_mask() {
        assumeTrue(System.getProperty("os.name").contains("Linux"));
        // ...
    }

    @Test
    public void test_group_shape_with_mask() {
        assumeTrue(System.getProperty("os.name").contains("Linux"));
        // ...
    }
}
```