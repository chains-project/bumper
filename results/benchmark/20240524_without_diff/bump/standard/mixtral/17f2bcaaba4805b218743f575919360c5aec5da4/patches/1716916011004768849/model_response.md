Here's the modified version of the code that fixes the issue:

```java
_radialWarp() {
    boolean groupChildrenEqualTwo = GROUP.getChildCount() == 2;
    micycle.pgs.Assertions.assertTrue(groupChildrenEqualTwo);
    processing.core.PShape out = micycle.pgs.PGS;
    _Morphology.radialWarp(GROUP, 10, 1, false);
    micycle.pgs.Assertions.assertEquals(2, out.getChildCount());
}
```

I fixed the issue by removing the '=' sign from the `assertTrue` and `assertEquals` function calls. Additionally, I created a new variable `groupChildrenEqualTwo` to store the result of the comparison to make the code more readable.