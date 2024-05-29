Here's the fixed method with the issue resolved. I replaced the illegal character '\' with a legal one:

```java
_radialWarp() {
    micycle.pgs.Assertions.assertTrue(GROUP == _SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS;
    _Morphology.radialWarp(GROUP = _SHAPE, 10, 1, false);
    micycle.pgs.Assertions.assertEquals(2, out.getChildCount());
}
```