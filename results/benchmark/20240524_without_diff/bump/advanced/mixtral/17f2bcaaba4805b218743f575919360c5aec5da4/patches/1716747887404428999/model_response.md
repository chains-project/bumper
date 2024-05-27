Here is a proposed patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_radialWarp() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    assertEquals(2, out.getChildCount());
}
```

The failure is caused by the fact that the method `org.junit.Assume.assumeTrue` is not present in the JUnit 5 library. In JUnit 5, the equivalent method is `org.junit.jupiter.api.Assertions.assertTrue`.

In this patch, the method `org.junit.Assume.assumeTrue` is replaced with `org.junit.jupiter.api.Assertions.assertTrue`, which has the same behavior.

Additionally, the import statements for `assertEquals` and `assertTrue` are added to make the code more readable.

Note that the function signature is not changed, and no external dependencies are added.