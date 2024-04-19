Here's a proposed patch to fix the failing test:
```java
@Test
void test_PGS_Morphology_buffer() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Morphology.buffer(GROUP_SHAPE, -1, true);
    assertEquals(2, out.getChildCount());
}
```
The patch adds a third argument `true` to the `PGS_Morphology.buffer()` method, which fixes the error by providing the correct buffer size.