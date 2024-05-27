Here's the patched code that uses `org.junit.jupiter.api.Assertions.assertTrue` instead of `Assume.assumeTrue` since the latter is not available in the provided code:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_chaikinCut() {
    org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.chaikinCut(GROUP_SHAPE, 0.5, 2);
    assertEquals(2, out.getChildCount());
}
```
This code should resolve the "cannot find symbol" error.