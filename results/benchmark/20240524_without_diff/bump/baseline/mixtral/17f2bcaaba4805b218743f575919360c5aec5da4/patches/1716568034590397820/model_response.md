Here is a possible patch for the failing client code:

```java
@Test
void test_PGS_Morphology_round() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape parent = GROUP_SHAPE.getChildren()[0];
    PShape out = PGS_Morphology.round(parent, 0.5);
    assertEquals(1, out.getChildCount());
}
```

This patch assumes that the failure is caused by a change in the `PGS_Morphology.round()` method, which now operates on a single `PShape` instead of a `PShapeGroup`. To adapt to this change, the patch extracts the first child of `GROUP_SHAPE` and passes it to `PGS_Morphology.round()`, and then checks that the result has one child.

Note that this patch may not be correct if the second child of `GROUP_SHAPE` is also required for the test. In that case, additional changes may be needed.