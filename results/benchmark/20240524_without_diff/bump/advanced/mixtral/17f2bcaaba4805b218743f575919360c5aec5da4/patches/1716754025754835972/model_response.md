Here's the fixed code for the `test_PGS_Morphology_smoothGaussian` method:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_smoothGaussian() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

In the original code, the method `org.junit.Assume.assumeTrue` was used, but it should have been `org.junit.jupiter.api.Assertions.assumeTrue`. I replaced the incorrect method call with the correct one.