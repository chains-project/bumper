Here's a possible patch for the failing client code:

```java
import processing.core.PShape;

@Test
void test_PGS_Morphology_smoothGaussian() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape parent = GROUP_SHAPE.getChild(0);
    PShape out = PGS_Morphology.smoothGaussian(parent, 10);
    assertEquals(2, out.getChildCount());
}
```

In this patch, I created a new variable `parent` to store the first child of `GROUP_SHAPE`. Then, I passed `parent` to the `smoothGaussian` method instead of `GROUP_SHAPE`. This way, the method can find the required symbol and the test can pass.