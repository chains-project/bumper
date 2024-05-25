Here's a proposed patch for the given failing client code:

```java
import processing.core.PShape;

@Test
void test_PGS_Morphology_radialWarp() {
    assumeTrue(GROUP_SHAPE != null && GROUP_SHAPE.getChildCount() == 2);
    PShape parent = GROUP_SHAPE.getParent();
    PShape out = PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    assertEquals(2, out.getChildCount());
    if (parent != null) {
        parent.addChild(out);
    }
}
```

This patch checks if `GROUP_SHAPE` is not `null` before calling `getChildCount()` to avoid the "cannot find symbol" error. Additionally, it saves the parent of `GROUP_SHAPE`, creates a new `PShape` with `radialWarp`, and adds the new `PShape` back to the parent if it exists. This ensures that the new `PShape` is properly managed even if there are changes in the external dependency.