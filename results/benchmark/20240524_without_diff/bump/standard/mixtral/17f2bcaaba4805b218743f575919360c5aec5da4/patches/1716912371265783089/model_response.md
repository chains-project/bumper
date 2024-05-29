Here's a fixed version of the code that uses `Assertions.assumeTrue` instead of the deprecated `Assume.assumeTrue`:

```java
import static org.junit.jupiter.api.Assertions.assumeTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_fieldWarp() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.fieldWarp(GROUP_SHAPE, 10, 1, false);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

Note that you need to import `assumeTrue` statically from `org.junit.jupiter.api.Assertions`.