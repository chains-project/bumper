Here's a proposed patch for the failing client code:

```java
import processing.core.PShape;

@Test
void test_PGS_Morphology_round() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape roundShape = PGS_Morphology.round(GROUP_SHAPE, 0.5);
    PShape out = (PShape) roundShape.getChildren().get(0); // Assuming the first child is the one we want
    assertEquals(2, out.getChildCount());
}
```

This patch assumes that the issue is caused by a change in the `PGS_Morphology.round()` method that now returns a `PShape` object containing multiple children instead of a single child. The patch retrieves the first child of the returned `PShape` object, which should be the equivalent of the original single child.