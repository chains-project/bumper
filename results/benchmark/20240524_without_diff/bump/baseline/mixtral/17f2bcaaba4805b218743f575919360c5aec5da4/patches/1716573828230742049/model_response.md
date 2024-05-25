Here's the fixed version of the failing client code:

```java
import processing.core.PShape;
import static processing.core.PConstants.CLOSE;

@Test
void test_PGS_Morphology_minkSum() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    final var mink = new PShape(PShape.PATH);
    mink.beginShape();
    mink.vertex(0, 0);
    mink.vertex(5, 0);
    mink.vertex(5, 5);
    mink.vertex(0, 5);
    mink.endShape(CLOSE);

    var out = PGS_Morphology.minkSum(GROUP_SHAPE, mink);
    assertEquals(2, out.getChildCount());
}
```

The only change made is the usage of `var` instead of `final PShape` for the `mink` variable. This should fix the issue without changing the functionality of the code.