Here is a proposed patch for the failing client code:
```java
_erosionDilation() {
    Assume.assumeTrue(Morphology.GROUP_SHAPE.getChildCount() == 2);
    PShape out = Morphology.erosionDilation(Morphology.GROUP_SHAPE, 0);
    Assertions.assertEquals(2, out.getChildCount());
}
```
The only change made is to replace the deprecated `assertEquals` method with the equivalent method from the `Assertions` class. This should resolve the "illegal character" error, as the backslash character is used in Java to escape certain special characters, and was likely causing a syntax error in this case.