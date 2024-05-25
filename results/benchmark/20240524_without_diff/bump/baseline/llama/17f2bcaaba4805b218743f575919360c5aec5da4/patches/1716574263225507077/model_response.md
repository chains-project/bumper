```java
@Test
void test_PGS_Processing_densify() {
    PShape groupShape = GROUP_SHAPE;
    assumeTrue(groupShape.getChildCount() == 2);
    PShape out = PGS_Processing.densify(groupShape, 1);
    assertEquals(2, out.getChildCount());
}
```