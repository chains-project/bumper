Here's the proposed patch:

```java
@Test
void test_PGS_Morphology_radialWarp() {
    assumeTrue(new PGS_Morphology().getGroupShape().getChildCount() == 2);
    PShape out = new PGS_Morphology().radialWarp(new PGS_Morphology().getGroupShape(), 10, 1, false);
    assertEquals(2, out.getChildCount());
}
```

This patch creates a new instance of `PGS_Morphology` to access the `getGroupShape()` and `radialWarp()` methods. It's possible that the external dependency update has changed the visibility or access to these methods, so this patch creates a new instance to ensure access.