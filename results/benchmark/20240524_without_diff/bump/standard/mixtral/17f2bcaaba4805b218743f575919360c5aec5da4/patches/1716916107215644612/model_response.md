Here's the fixed method with the issue resolved:
```java
_radialWarp() {
    boolean groupChildrenEqualTwo = _SHAPE.getChildCount() == 2;
    micycle.pgs.Assertions.assertTrue("GROUP should have 2 children", groupChildrenEqualTwo);
    processing.core.PShape out = micycle.pgs.PGS;
    _Morphology.radialWarp(GROUP: _SHAPE, 10, 1, false);
    int outChildCount = out.getChildCount();
    micycle.pgs.Assertions.assertEquals("Out should have 2 children", 2, outChildCount);
}
```
The issue was caused by using the '=' operator in the assertion methods, which should use '==' for comparison and use a descriptive error message. Also, it is a good practice to declare and assign variables on separate lines for better readability.