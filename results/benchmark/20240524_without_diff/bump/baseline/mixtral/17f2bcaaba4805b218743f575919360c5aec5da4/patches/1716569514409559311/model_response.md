Here's a proposed patch for the failing client code:

```java
@Test
void test_PGS_Morphology_chaikinCut() {
    assumeTrue(MorphologyGroupShape.getChildCount() == 2);
    PShape parentShape = new PShape(PShape.GROUP);
    parentShape.addChild(MorphologyGroupShape.getChild(0));
    parentShape.addChild(MorphologyGroupShape.getChild(1));
    PShape out = PGS_Morphology.chaikinCut(parentShape, 0.5, 2);
    assertEquals(2, out.getChildCount());
}
```

This patch creates a new `PShape` object as a parent for the children of `MorphologyGroupShape`. This should fix the issue with the missing symbol, as the new `PShape` object can be used in place of the missing `GROUP_SHAPE`.