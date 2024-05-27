Here's the fixed method with the necessary import statement added:

```java
import static org.junit.jupiter.api.Assertions.assumeTrue;
import org.junit.jupiter.api.Test;

void test_PGS_Morphology_round() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The `assumeTrue` method is part of the `org.junit.jupiter.api.Assumptions` class, but it can be imported statically into the test class for convenience.