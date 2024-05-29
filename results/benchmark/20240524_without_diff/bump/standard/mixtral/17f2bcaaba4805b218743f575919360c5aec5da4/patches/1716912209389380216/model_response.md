Here is a fixed version of the code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_erosionDilation() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    assertEquals(2, out.getChildCount());
}
```

The issue is that the `assumeTrue` method is not being imported. I added the necessary import statement at the top of the file.