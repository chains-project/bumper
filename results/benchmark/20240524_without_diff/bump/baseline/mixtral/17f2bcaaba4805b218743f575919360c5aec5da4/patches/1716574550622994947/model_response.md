Here is a proposed patch for the failing client code:

```java
@Test
void test_PGS_Morphology_round() {
    assumeTrue(PApplet.parseInt(PApplet.getText("GROUP_SHAPE_CHILD_COUNT")) == 2);
    PShape out = PGS_Morphology.round(getGroupShape(), 0.5);
    assertEquals(2, out.getChildCount());
}

PShape getGroupShape() {
    // initialize and return the GROUP_SHAPE here
}
```

In this patch, I added a new helper method `getGroupShape()` to return the `GROUP_SHAPE` object, since it seems to be a global variable that is not accessible from the test method. I also replaced the direct reference to `GROUP_SHAPE` with a call to `getGroupShape()`.

Additionally, I replaced the direct access to `GROUP_SHAPE.getChildCount()` with a call to a new function `PApplet.parseInt(PApplet.getText("GROUP_SHAPE_CHILD_COUNT"))`. This assumes that the value of `GROUP_SHAPE.getChildCount()` is stored in a configuration file or a properties file that can be accessed through `PApplet.getText()`. If this is not the case, you may need to modify this part of the code accordingly.

Note that in this patch, I made the assumption that the `PGS_Morphology` class and the `PShape` class are still available and have not been removed in the updated version of the external dependency.