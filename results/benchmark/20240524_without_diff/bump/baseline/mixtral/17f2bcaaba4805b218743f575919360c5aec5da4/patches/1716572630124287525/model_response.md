Here's a possible patch for the failing client code:

```java
import processing.core.PShape;

@Test
void test_PGS_Morphology_chaikinCut() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape parent = GROUP_SHAPE.getChildren()[0];
    float depth = 2;
    float fraction = 0.5;
    PShape out = PGS_Morphology.chaikinCut(parent, fraction, depth);
    assertEquals(2, out.getChildCount());
}
```

This patch declares the necessary variables for the method arguments and obtains the first child of the `GROUP_SHAPE` as the `parent` to pass to the `chaikinCut` method. This should resolve the "cannot find symbol" error.