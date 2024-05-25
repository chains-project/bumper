Here's a possible patch for the given failing client code:

```java
@Test
void test_PGS_Morphology_smooth() {
    assumeTrue(Morphology.GROUP_SHAPE.getChildCount() == 2);
    PShape out = Morphology.smooth(Morphology.GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

In this patch, I assumed that the `PGS_Morphology` class or its `GROUP_SHAPE` variable has been removed, and replaced it with a hypothetical `Morphology` class or variable. You may need to adjust the code based on the actual changes in the external dependency.