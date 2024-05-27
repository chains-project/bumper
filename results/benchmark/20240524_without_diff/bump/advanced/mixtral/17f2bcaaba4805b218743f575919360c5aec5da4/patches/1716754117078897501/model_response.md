Here's the fixed version of the code that removes the usage of the `Assume.assumeTrue` method, which is causing the error. I've replaced it with a simple `if` statement to ensure the test only runs when the condition is met.

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_smoothGaussian() {
    if (GROUP_SHAPE.getChildCount() != 2) {
        return;
    }
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

This code should resolve the "cannot find symbol" error caused by the `Assume.assumeTrue` method.