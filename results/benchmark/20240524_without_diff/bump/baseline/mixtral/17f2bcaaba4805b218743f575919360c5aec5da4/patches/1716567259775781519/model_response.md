Here's a fixed version of the method. I added a check to ensure that the `PGS_Morphology` class is not null, which might be causing the "cannot find symbol" error:

```java
@Test
void test_PGS_Morphology_minkSum() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    final PShape mink = new PShape(PShape.PATH);
    mink.beginShape();
    mink.vertex(0, 0);
    mink.vertex(5, 0);
    mink.vertex(5, 5);
    mink.vertex(0, 5);
    mink.endShape(PConstants.CLOSE);

    PGS_Morphology morphology = new PGS_Morphology(); // add this line
    assertNotNull(morphology); // add this line

    PShape out = morphology.minkSum(GROUP_SHAPE, mink);
    assertEquals(2, out.getChildCount());
}
```

This code assumes that the `PGS_Morphology` class is not being properly instantiated, causing a null pointer exception that results in the "cannot find symbol" error. This code creates a new instance of `PGS_Morphology` and checks that it is not null before calling the `minkSum` method.