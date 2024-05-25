```java
@Test
void test_PGS_Processing_removeSmallHoles() {
    PShape GROUP_SHAPE = new PShape();
    GROUP_SHAPE.addChild(new PShape());
    GROUP_SHAPE.addChild(new PShape());
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Processing.removeSmallHoles(GROUP_SHAPE, 10);
    assertEquals(2, out.getChildCount());
}
```