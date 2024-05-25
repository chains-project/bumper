Here is a possible patch for the failing client code:
```java
@Test
void test_PGS_Morphology_simplifyVW() {
    assumeTrue(micycle.pgs.PGS_ShapeFactory.GROUP_SHAPE.getChildCount() == 2);
    PShape out = micycle.pgs.PGS_Morphology.simplifyVW(micycle.pgs.PGS_ShapeFactory.GROUP_SHAPE, 1);
    assertEquals(2, out.getChildCount());
}
```
This patch assumes that the missing symbol is the `GROUP_SHAPE` object, which is presumably defined in the `PGS_ShapeFactory` class. By fully qualifying the name of `GROUP_SHAPE`, the code should be able to find the symbol and compile without errors.

Note that this patch assumes that the `PGS_ShapeFactory` class and the `simplifyVW` method are still available and unchanged in the new version of the external dependency. If this is not the case, then a different solution may be necessary.