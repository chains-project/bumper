Here's the proposed patch:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_smoothGaussian() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
    assertEquals(2, out.getChildCount());
}
```

The issue is caused by the missing import statement for `org.junit.jupiter.api.Assumptions`. I added the necessary import statement and updated the import of `assertEquals` to be fully qualified.