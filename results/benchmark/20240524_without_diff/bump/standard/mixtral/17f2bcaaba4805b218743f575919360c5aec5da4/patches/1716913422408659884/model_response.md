Here's the patched code that fixes the error:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    assertEquals(2, out.getChildCount());
}
```

In the original code, the method `org.junit.Assume.assumeTrue` was used, but it is not part of JUnit 5, which is likely the version being used in this case. I replaced it with the method `org.junit.jupiter.api.Assertions.assertTrue`, which checks if the condition is true and fails the test if it's not. This should resolve the "cannot find symbol" error.