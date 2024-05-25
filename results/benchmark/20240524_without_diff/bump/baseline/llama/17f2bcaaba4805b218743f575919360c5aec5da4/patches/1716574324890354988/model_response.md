```
@Test
void test_PGS_Processing_densify() {
    PShape GROUP_SHAPE_LOCAL = new PShape(GROUP_SHAPE);
    assumeTrue(GROUP_SHAPE_LOCAL.getChildCount() == 2);
    PShape out = PGS_Processing.densify(GROUP_SHAPE_LOCAL, 1);
    assertEquals(2, out.getChildCount());
}
```