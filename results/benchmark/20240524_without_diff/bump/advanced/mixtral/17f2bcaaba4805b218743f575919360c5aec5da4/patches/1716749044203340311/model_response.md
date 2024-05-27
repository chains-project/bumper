Here is a fixed version of the code that should resolve the error:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

In this version, I replaced the `assumeTrue` method with `assertTrue`, which has the same behavior but does not throw an error if the condition is not met. This should resolve the "cannot find symbol" error.