```java
@Test
void test_PGS_Processing_removeSmallHoles() {
    if (!(GROUP_SHAPE.getChildCount() == 2)) return;
    PShape out = PGS_Processing.removeSmallHoles(GROUP_SHAPE, 10);
    assertEquals(2, out.getChildCount());
}
```