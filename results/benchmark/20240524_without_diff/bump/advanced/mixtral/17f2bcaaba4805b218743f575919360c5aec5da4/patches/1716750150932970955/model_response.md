Here's the fixed `test_PGS_Morphology_round` method:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The fix is to replace `org.junit.Assume.assumeTrue` with `org.junit.jupiter.api.Assertions.assumeTrue`. The issue was caused by using the wrong import for `assumeTrue`.