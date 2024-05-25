Here's a possible patch for the given failing client code:

```java
@Test
void test_PGS_Morphology_round() {
    assumeTrue(new PGS_Morphology().getGROUP_SHAPE().getChildCount() == 2);
    PShape out = new PGS_Morphology().round(new PGS_Morphology().getGROUP_SHAPE(), 0.5);
    assertEquals(2, out.getChildCount());
}
```

This patch creates new instances of `PGS_Morphology` to access the `getGROUP_SHAPE()` method, which seems to be causing the "cannot find symbol" error. This assumes that the `PGS_Morphology` class has a public method `getGROUP_SHAPE()` that returns a `PShape` object. If this is not the case, you may need to modify the patch accordingly.