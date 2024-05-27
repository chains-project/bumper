Here's a fixed version of the code, replacing the failing `Assume.assumeTrue` call with a JUnit 5 `assertAll` call, which checks if the condition is true:

```java
import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyTopology() {
    assertAll(
        () -> assertTrue(GROUP_SHAPE.getChildCount() == 2)
    );
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

This code imports the necessary static methods from JUnit 5 and uses `assertAll` to check the condition. If the condition is false, `assertAll` will throw an `AssertionError`.