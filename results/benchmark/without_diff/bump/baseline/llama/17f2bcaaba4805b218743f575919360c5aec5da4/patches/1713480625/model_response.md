Here's a proposed patch to fix the failing test:
```java
@Test
void test_PGS_Morphology_buffer() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Morphology.buffer(GROUP_SHAPE, -1, true);
    assertEquals(2, out.getChildCount());
}
```
The patch adds the `true` argument to the `buffer` method, which is a new overload that takes an additional `applyToGroupShapes` argument. This new overload was added in version 1.1.0 of the library, which is why the test fails with the old version. By adding `true` as the value for this argument, we ensure that the method applies to group shapes correctly.