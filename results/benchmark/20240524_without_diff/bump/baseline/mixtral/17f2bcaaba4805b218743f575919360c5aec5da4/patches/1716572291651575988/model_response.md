Here's the proposed patch for the failing client code:

```java
import processing.core.PShape;

@Test
void test_PGS_Morphology_buffer() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Morphology.buffer(GROUP_SHAPE, -1.0); // Changed int to double
    assertEquals(2, out.getChildCount());
}
```

In this patch, I changed the int argument in the `PGS_Morphology.buffer()` method to a double, since it's possible that the external dependency update might have changed the method signature. This should resolve the "cannot find symbol" error.