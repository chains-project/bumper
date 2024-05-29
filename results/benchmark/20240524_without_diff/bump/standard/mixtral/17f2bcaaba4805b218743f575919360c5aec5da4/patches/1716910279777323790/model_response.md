Here's the fixed method with the necessary import statement:
```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_chaikinCut() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.chaikinCut(GROUP_SHAPE, 0.5, 2);
    assertEquals(2, out.getChildCount());
}
```
The issue was caused by the missing import statement for `assumeTrue`. I added the necessary import statement to fix the error.