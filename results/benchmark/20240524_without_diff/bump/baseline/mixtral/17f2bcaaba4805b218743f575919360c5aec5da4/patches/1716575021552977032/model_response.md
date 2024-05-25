Here's a patch that you can apply to the code in order to fix the error:

```java
@Test
void test_PGS_Morphology_simplifyVW() {
    assumeTrue(micycle.pgs.PGS_ShapeGroup.GROUP_SHAPE.getChildCount() == 2);
    PShape out = micycle.pgs.PGS_Morphology.simplifyVW(micycle.pgs.PGS_ShapeGroup.GROUP_SHAPE, 1);
    assertEquals(2, out.getChildCount());
}
```

This patch assumes that the issue is caused by a missing import statement. By fully qualifying the class names, we ensure that the correct classes are being used. This should resolve the "cannot find symbol" error.