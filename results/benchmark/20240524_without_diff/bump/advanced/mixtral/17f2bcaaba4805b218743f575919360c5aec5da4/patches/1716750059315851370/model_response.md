Here's the fixed version of the code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

The issue was that the `Assume` class was not imported properly. I imported the missing class and changed the import of the `assertEquals` method to use a static import.