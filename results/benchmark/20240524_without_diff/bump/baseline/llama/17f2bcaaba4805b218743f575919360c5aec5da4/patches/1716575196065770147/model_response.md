```java
@Test
void test_PGS_Processing_convexPartition() {
    PShape groupShape = new PShape();
    groupShape.addChild(new PShape());
    groupShape.addChild(new PShape());
    assumeTrue(groupShape.getChildCount() == 2);
    PShape out = PGS_Processing.convexPartition(groupShape);
    assertEquals(2, out.getChildCount());
}
```