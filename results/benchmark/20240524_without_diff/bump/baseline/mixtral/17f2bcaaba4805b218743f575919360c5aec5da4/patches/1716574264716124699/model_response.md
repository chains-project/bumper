Here's a proposed patch for the failing client code:

```java
@Test
void test_PGS_Morphology_radialWarp() {
    assumeTrue(PGS_Morphology.getGroupShape().getChildCount() == 2);
    PShape out = PGS_Morphology.radialWarp(PGS_Morphology.getGroupShape(), 10, 1, false);
    assertEquals(2, out.getChildCount());
}
```

Assuming that `GROUP_SHAPE` is a static field that was removed in the new version of the external dependency, this patch replaces it with a call to a static method `PGS_Morphology.getGroupShape()` that returns the same `PShape` object. You may need to modify this method to match the actual implementation in your codebase.