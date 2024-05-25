Here's the proposed patch for the failing client code:

```java
import processing.core.PShape;

import static org.junit.Assert.assertEquals;
import static org.junit.Assume.assumeTrue;

@Test
void test_PGS_Morphology_round() {
    assumeTrue(PGS_Morphology.getGroupShapeChildCount(GROUP_SHAPE) == 2);
    PShape out = PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, PGS_Morphology.getGroupShapeChildCount(out));
}
```

In this patch, I added a static method `getGroupShapeChildCount` to the `PGS_Morphology` class to get the child count of a `PShape` group. This is because I assumed that the `getChildCount` method is not available for `PShape` objects in the new version. The patch also modifies the `assumeTrue` and `assertEquals` statements to use the new method.

Assuming that the `PGS_Morphology` class is under your control, you can add the following method to it:

```java
public static int getGroupShapeChildCount(PShape groupShape) {
    return groupShape.getChildCount();
}
```

This method simply delegates to the `getChildCount` method of the `PShape` object.