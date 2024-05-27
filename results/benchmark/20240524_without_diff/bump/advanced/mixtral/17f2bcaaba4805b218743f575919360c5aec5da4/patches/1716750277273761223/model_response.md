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

The issue was that the import statement for `Assumptions` was missing. I added the following import statement to fix the issue:

```java
import static org.junit.jupiter.api.Assumptions.assumeTrue;
```