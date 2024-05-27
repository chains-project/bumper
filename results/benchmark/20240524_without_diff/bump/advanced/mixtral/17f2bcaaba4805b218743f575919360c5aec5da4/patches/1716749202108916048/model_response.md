Here's the patched version of the method using `org.junit.jupiter.api.Assertions.assertTrue` instead of `org.junit.Assume.assumeTrue`:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplify() {
    org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplify(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

This should resolve the "cannot find symbol" error.