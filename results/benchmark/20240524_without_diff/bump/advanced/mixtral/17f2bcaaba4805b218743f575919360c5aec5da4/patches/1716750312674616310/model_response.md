Here is a fixed version of the code that should resolve the error:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyTopology() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
    assertEquals(2, out.getChildCount());
}
```

In this fixed version, I added the necessary import statements for `assumeTrue` and `assertEquals` methods. These import statements allow the compiler to find the missing symbols and resolve the error.