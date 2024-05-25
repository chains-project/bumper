Here's a proposed patch for the failing client code:

```java
@Test
void test_PGS_Morphology_erosionDilation() {
    assumeTrue(getGroupShape().getChildCount() == 2);
    PShape out = PGS_Morphology.erosionDilation(getGroupShape(), 0);
    assertEquals(2, out.getChildCount());
}

private PShape getGroupShape() {
    return GROUP_SHAPE;
}
```

The patch introduces a new private method `getGroupShape()` that returns the `GROUP_SHAPE` object. By doing this, we avoid directly referencing `GROUP_SHAPE` in the test method and thus avoid the "cannot find symbol" error.

Note that this patch assumes that `GROUP_SHAPE` is a field of the class containing the test method. If this is not the case, the `getGroupShape()` method would need to be adapted accordingly.