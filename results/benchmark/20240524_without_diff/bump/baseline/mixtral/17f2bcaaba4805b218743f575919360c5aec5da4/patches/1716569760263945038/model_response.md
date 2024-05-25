Here is a possible patch for the failing client code:

```java
@Test
void test_PGS_Morphology_erosionDilation() {
    assumeTrue(Morphology.GROUP_SHAPE.getChildCount() == 2);
    PShape out = Morphology.erosionDilation(Morphology.GROUP_SHAPE, 0);
    assertEquals(2, out.getChildCount());
}
```

This patch assumes that the class `Morphology` has been added in the new version of the library, and that it contains a static field `GROUP_SHAPE` and a static method `erosionDilation()`. If this is not the case, you may need to adjust the patch accordingly.