```java
@org.junit.jupiter.api.Test
void test_PGS_Processing_removeSmallHoles() {
    org.junit.Assume.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Processing.removeSmallHoles(GROUP_SHAPE, 10);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```