```java
@org.junit.jupiter.api.Test
void test_PGS_Processing_convexPartition() {
    org.junit.jupiter.api.Assumptions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Processing.convexPartition(GROUP_SHAPE);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```