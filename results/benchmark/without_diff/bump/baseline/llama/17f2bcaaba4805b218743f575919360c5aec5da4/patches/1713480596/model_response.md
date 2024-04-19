Here's a proposed patch to fix the failing test:
```java
@Test
void test_PGS_Morphology_buffer() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Morphology.buffer(GROUP_SHAPE, -1, PGS_Morphology.getDefaultMorphology());
    assertEquals(2, out.getChildCount());
}
```
The patch adds the `PGS_Morphology.getDefaultMorphology()` method call to the `PGS_Morphology.buffer()` method call. This is to provide a default morphology instance, as the method signature has changed and now requires a morphology instance as the third parameter.

The `PGS_Morphology.getDefaultMorphology()` method call returns a default morphology instance that can be used when no morphology instance is provided. This should fix the issue of the failing test.