Here's the fixed version of the code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_buffer() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.buffer(GROUP_SHAPE, -1);
    assertEquals(2, out.getChildCount());
}
```

The issue is caused by a missing import statement for `assumeTrue`. I added the necessary import statement to the top of the file.