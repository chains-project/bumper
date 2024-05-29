Here's the updated client code to fix the error:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;
import org.junit.jupiter.api.Test;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    assertEquals(2, out.getChildCount());
}
```

The issue was that the `assumeTrue` method was not being imported properly. I've added the necessary import statement for `org.junit.jupiter.api.Assumptions.assumeTrue`.