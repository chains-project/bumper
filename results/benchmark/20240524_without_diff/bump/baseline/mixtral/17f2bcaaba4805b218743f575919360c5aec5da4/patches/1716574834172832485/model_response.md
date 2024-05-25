Here is a possible patch for the failing client code:

```java
@Test
void test_PGS_Morphology_simplifyVW() {
    assumeTrue(micycle.pgs.PGS_ShapeGroup.GROUP_SHAPE.getChildCount() == 2);
    PShape out = micycle.pgs.PGS_Morphology.simplifyVW(micycle.pgs.PGS_ShapeGroup.GROUP_SHAPE, 1);
    assertEquals(2, out.getChildCount());
}
```

This patch assumes that the missing symbol is a class or variable named `GROUP_SHAPE` in the `micycle.pgs.PGS_ShapeGroup` class. By fully qualifying the reference to `GROUP_SHAPE`, we can ensure that the correct symbol is being referenced.

Note that this patch assumes that the `simplifyVW` method and the `assertEquals` method are still available and unchanged in the updated version of the external dependency. If this is not the case, further modifications to the client code may be necessary.