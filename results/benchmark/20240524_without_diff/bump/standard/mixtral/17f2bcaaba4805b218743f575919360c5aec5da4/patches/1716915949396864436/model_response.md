Here's the updated method with the error fixed:

```java
_radialWarp() {
    micycle.pgs.Assertions.assertTrue(GROUP == _SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS.createShape(micycle.pgs.PGS.GROUP);
    _Morphology.radialWarp(GROUP, _SHAPE, 10, 1, false);
    micycle.pgs.Assertions.assertEquals(2, out.getChildCount());
}
```

Changes made:
1. Replaced the single '=' with double '==' for comparison inside the assertTrue method.
2. Changed the method signature of _Morphology.radialWarp() by passing GROUP and _SHAPE separately.
3. Created a new PShape object 'out' using micycle.pgs.PGS.createShape() method.
4. Fixed the method call to _Morphology.radialWarp() by passing separate arguments.