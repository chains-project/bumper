Here's the fixed method with the illegal character removed:
```java
_radialWarp() {
    micycle.pgs.Assertions.assertTrue(GROUP == _SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS;
    _Morphology.radialWarp(GROUP = _SHAPE, 10, 1, false);
    micycle.pgs.Assertions.assertEquals(2, out.getChildCount());
}
```
In the original code, the `=` sign was replaced with `\=`, which is not a valid character in Java. I replaced it back with `=` to fix the error.