```java
@Test
void test_PGS_Processing_removeSmallHoles() {
    PShape GROUP_SHAPE = PGS_Processing.createGroupShape();
    GROUP_SHAPE.addChild(PGS_Processing.createShape(10, 10, 20, 20));
    GROUP_SHAPE.addChild(PGS_Processing.createShape(30, 30, 40, 40));
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Processing.removeSmallHoles(GROUP_SHAPE, 10);
    assertEquals(2, out.getChildCount());
}
```