Here is a fixed version of the method that should resolve the error:

```java
@Test
void test_PGS_Morphology_minkSum() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape mink = createShape(PATH);
    beginShape(mink);
    vertex(0, 0);
    vertex(5, 0);
    vertex(5, 5);
    vertex(0, 5);
    endShape(CLOSE);

    PShape out = PGS_Morphology.minkSum(GROUP_SHAPE, mink);
    assertEquals(2, out.getChildCount());
}
```

The only change I made was to replace the line
`final PShape mink = new PShape(PShape.PATH);`
with
`PShape mink = createShape(PATH);`
`beginShape(mink);`

It appears that the constructor `new PShape(int)` has been removed, and replaced with the static method `createShape(int)` and the instance method `beginShape()`.