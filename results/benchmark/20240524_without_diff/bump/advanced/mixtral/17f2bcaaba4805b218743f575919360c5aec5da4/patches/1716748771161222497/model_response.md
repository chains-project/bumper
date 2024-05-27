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

The error was caused by the use of the `org.junit.Assume.assumeTrue` method, which is not part of JUnit 5. I replaced it with `org.junit.jupiter.api.Assertions.assertTrue`, which has the same behavior.

Note that I also imported the `assertEquals` and `assertTrue` methods statically to make the code more concise.