Here's the fixed failing method with the error resolved:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The change made is replacing `org.junit.Assume.assumeTrue` with `org.junit.jupiter.api.Assertions.assumeTrue`. The issue was caused by using the wrong import for the `assumeTrue` method.