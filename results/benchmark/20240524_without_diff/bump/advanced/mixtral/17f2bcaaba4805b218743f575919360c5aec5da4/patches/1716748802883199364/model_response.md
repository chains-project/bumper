Here's the fixed method with the required import statement added:

```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The error was caused by using `org.junit.Assume.assumeTrue` instead of `org.junit.jupiter.api.Assertions.assertTrue`. The `assumeTrue` method is used to conditionally ignore tests based on some assumptions, while `assertTrue` is used to check if a condition is true and fail the test if it's not. In this case, `assertTrue` is the correct method to use.