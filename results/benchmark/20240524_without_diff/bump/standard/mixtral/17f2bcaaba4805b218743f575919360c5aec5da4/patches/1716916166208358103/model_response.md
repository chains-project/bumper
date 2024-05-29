Here's the fixed `_radialWarp` method with illegal character removed:

```java
_radialWarp() {
    micycle.pgs.Assertions.assertTrue(GROUP == _SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS;
    _Morphology.radialWarp(GROUP = _SHAPE, 10, 1, false);
    micycle.pgs.Assertions.assertEquals(2, out.getChildCount());
}
```

The `=` sign was replaced with `==` in the first line to fix the illegal character error.