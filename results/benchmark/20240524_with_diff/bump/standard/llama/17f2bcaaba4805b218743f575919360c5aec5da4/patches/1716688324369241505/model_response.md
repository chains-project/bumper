Here is the patched code:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_radialWarp() {
    org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```