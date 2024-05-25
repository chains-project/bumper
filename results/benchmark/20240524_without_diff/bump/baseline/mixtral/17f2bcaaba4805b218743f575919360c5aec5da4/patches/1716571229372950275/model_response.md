Here is a possible patch for the failing client code:

```java
import processing.core.PShape;

@Test
void test_PGS_Morphology_round() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape parent = GROUP_SHAPE.getChildren()[0];
    float radius = 0.5f;
    PShape out = PGS_Morphology.round(parent, radius);
    assertEquals(1, out.getChildCount());
    PShape circle = out.getChildren()[0];
    assertEquals(360, circle.getVertexCount());
    assertEquals(radius, circle.getVertex(0).x, 0.01);
    assertEquals(radius, circle.getVertex(0).y, 0.01);
}
```

This patch assumes that the failure is caused by a change in the `PGS_Morphology.round` method, which now returns a single `PShape` object instead of a group of shapes. The patch creates a new variable `parent` to refer to the first child of `GROUP_SHAPE`, and passes it to `PGS_Morphology.round` along with a `radius` of 0.5. It then checks that the output `out` is a single shape with 360 vertices, and that the first vertex of `out` is at the expected position.

Note that this patch is just a guess based on the provided information, and it may not fix the actual failure. To confirm that the patch works, you should compile and test it with the updated version of the external dependency.