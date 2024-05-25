```java
@Test
void test_PGS_Processing_removeSmallHoles() {
    PShape GROUP_SHAPE = PGS_Processing.createGroup();
    GROUP_SHAPE.addChild(PGS_Processing.createShape());
    GROUP_SHAPE.addChild(PGS_Processing.createShape());
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Processing.removeSmallHoles(GROUP_SHAPE, 10);
    assertEquals(2, out.getChildCount());
}
```