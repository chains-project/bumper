Here's the proposed patch:

```java
@Test
void test_PGS_Morphology_minkSum() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape mink = createShape(PShape.PATH);
    beginShape(mink);
    vertex(0, 0);
    vertex(5, 0);
    vertex(5, 5);
    vertex(0, 5);
    endShape(mink, PConstants.CLOSE);

    PShape out = PGS_Morphology.minkSum(GROUP_SHAPE, mink);
    assertEquals(2, out.getChildCount());
}
```

The changes made are:

* Replaced `new PShape(PShape.PATH)` with `createShape(PShape.PATH)`.
* Changed the order of arguments in `endShape()` method to `endShape(mink, PConstants.CLOSE)`.