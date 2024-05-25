```java
@Test
void test_PGS_Processing_convexPartition() {
    PShape GROUP_SHAPE_LOCAL = new PShape();
    GROUP_SHAPE_LOCAL.addChild(new PShape());
    GROUP_SHAPE_LOCAL.addChild(new PShape());
    assumeTrue(GROUP_SHAPE_LOCAL.getChildCount() == 2);
    PShape out = PGS_Processing.convexPartition(GROUP_SHAPE_LOCAL);
    assertEquals(2, out.getChildCount());
}
```