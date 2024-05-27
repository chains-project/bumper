Here's the fixed version of the code, using `org.junit.jupiter.api.Assertions.assertAll` instead of `org.junit.Assume.assumeTrue`:

```java
import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assertAll(
        () -> assertEquals(2, GROUP_SHAPE.getChildCount()),
        () -> processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5),
        () -> assertEquals(2, out.getChildCount())
    );
}
```

This code checks that the child count of `GROUP_SHAPE` is 2 before calling `PGS_Morphology.round`, and then checks that the child count of the result is still 2. If the child count of `GROUP_SHAPE` is not 2, the test will fail immediately.

Note that this code assumes that the `GROUP_SHAPE` variable is defined and accessible in the test class. If `GROUP_SHAPE` is not defined, you will need to define it or replace it with a suitable `PShape` object.