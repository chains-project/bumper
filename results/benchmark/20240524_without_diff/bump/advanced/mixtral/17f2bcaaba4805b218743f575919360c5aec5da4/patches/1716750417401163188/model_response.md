Here's the fixed method with the error resolved:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyTopology() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The issue was caused by using `org.junit.Assume.assumeTrue` instead of `org.junit.jupiter.api.Assertions.assumeTrue`.