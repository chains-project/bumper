Here's the fixed method with the issue resolved:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_smooth() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The fix consists of replacing `org.junit.Assume.assumeTrue` with `org.junit.jupiter.api.Assertions.assumeTrue` to use the correct static method from JUnit Jupiter API.