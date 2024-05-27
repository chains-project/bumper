Here's a fixed version of the method using `assert` instead of `Assume.assumeTrue`:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    org.junit.jupiter.api.Assertions.assertAll(
        () -> org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2)
    );
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

This code uses `Assertions.assertAll` to assert that the condition is true, and it will fail the test if the condition is not met.