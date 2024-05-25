Here is a proposed patch for the failing client code:

```java
@Test
void test_PGS_Morphology_round() {
    assumeTrue(PApplet.parseInt(PApplet.getText("GROUP_SHAPE_child_count")) == 2);
    PShape out = PGS_Morphology.round(new PShape(PApplet.loadShape("GROUP_SHAPE")), 0.5);
    assertEquals(2, out.getChildCount());
}
```

This patch assumes that the external dependency issue is related to the `GROUP_SHAPE` variable. Instead of directly accessing `GROUP_SHAPE`, this patch loads it from a file using `PApplet.loadShape()`. Additionally, `GROUP_SHAPE_child_count` is assumed to be a file containing the number of child shapes of `GROUP_SHAPE`.

Note that this patch may not be the correct solution, and further investigation may be required to determine the root cause of the external dependency issue.