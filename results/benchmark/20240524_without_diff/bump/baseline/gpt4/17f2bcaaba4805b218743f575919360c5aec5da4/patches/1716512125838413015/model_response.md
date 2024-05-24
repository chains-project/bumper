```java
@Test
void test_PGS_Morphology_buffer() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Morphology.buffer(GROUP_SHAPE, -1);
    assertEquals(2, out.getChildCount());
}
```