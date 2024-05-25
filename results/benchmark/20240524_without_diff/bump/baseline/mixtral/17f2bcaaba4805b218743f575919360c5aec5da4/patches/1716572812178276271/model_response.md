Here's the proposed patch for the failing client code:

```java
@Test
void test_PGS_Morphology_chaikinCut() {
    assumeTrue(Morphology.GROUP_SHAPE.getChildCount() == 2);
    PShape out = Morphology.chaikinCut(Morphology.GROUP_SHAPE, 0.5, 2);
    assertEquals(2, out.getChildCount());
}
```

In this patch, I added the `Morphology.` prefix to the `GROUP_SHAPE` and `chaikinCut` references. This assumes that the `GROUP_SHAPE` and `chaikinCut` were moved or renamed in the external dependency. This is a common occurrence when updating dependencies, where the library developers may refactor or reorganize their code.

Note that I do not have enough information about the `PGS_Morphology` and `PGS_MorphologyGroupShapeTests` classes to make a more precise change. If the `GROUP_SHAPE` and `chaikinCut` references belong to these classes, then a different patch may be necessary. However, based on the information provided, this patch should resolve the "cannot find symbol" error.