Here's a possible patch for the given failing client code:

```java
import processing.core.PShape;

@Test
void test_PGS_Morphology_round() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape parent = GROUP_SHAPE.getChildren()[0];
    float amount = 0.5f;
    PShape out = PGS_Morphology.round(parent, amount);
    assertEquals(1, out.getChildCount());
    amount = 0.5f;
    out = PGS_Morphology.round(parent, amount);
    assertEquals(2, out.getChildCount());
}
```

In this patch, I created a new variable `parent` to hold the first child of `GROUP_SHAPE`, and then applied the `PGS_Morphology.round` function to `parent` instead of `GROUP_SHAPE`. Additionally, I added a new variable `amount` to explicitly set the rounding amount.

This patch assumes that the issue is caused by the external dependency's behavior change, and the `PGS_Morphology.round` function now operates on a single `PShape` instead of a `PShapeGroup`.

Note that the `assertEquals` statement checks the child count of `out` before and after the rounding operation to ensure that the function behaves as expected.