Here's the fixed method with the issue resolved:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_smoothGaussian() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The issue was caused by using `org.junit.Assume.assumeTrue` instead of `org.junit.jupiter.api.Assertions.assumeTrue`. I replaced the former with the latter to resolve the error.