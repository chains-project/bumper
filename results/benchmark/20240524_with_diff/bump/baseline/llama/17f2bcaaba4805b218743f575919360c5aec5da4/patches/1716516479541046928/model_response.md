```java
@Test
void test_PGS_Processing_convexPartition() {
    if (! (GROUP_SHAPE.getChildCount() == 2)) return;
    PShape out = PGS_Processing.convexPartition(GROUP_SHAPE);
    assertEquals(2, out.getChildCount());
}
```