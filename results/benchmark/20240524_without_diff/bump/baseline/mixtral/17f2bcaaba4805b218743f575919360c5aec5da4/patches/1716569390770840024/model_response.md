Here's a fixed version of the failing method. I created a new variable `shape` of type `PShape` to replace the `out` variable, which might have been removed in the updated version of the external library.

```java
@Test
void test_PGS_Morphology_chaikinCut() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape shape = PGS_Morphology.chaikinCut(GROUP_SHAPE, 0.5, 2);
    assertEquals(2, shape.getChildCount());
}
```

This solution assumes that the `chaikinCut` method still exists in the updated library but returns a `PShape` object instead of the original name `out`.