```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.condition.EnabledIfEnvironmentVariable;

public class PGS_MorphologyGroupShapeTests {

    @Test
    @EnabledIfEnvironmentVariable(named = "PGS_MORPHOLOGY_GROUP_SHAPE_TESTS", matches = "true")
    public void testGroupShape() {
        assumeTrue(PGS_MorphologyGroupShapeTests.class.getName().startsWith("micycle.pgs"));
    }
}
```