Here's the updated method with the required import statement:
```java
import static org.junit.jupiter.api.Assertions.assertTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyTopology() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```
The `assumeTrue` method is from JUnit 4, while the rest of the code uses JUnit 5. I replaced `assumeTrue` with `assertTrue` which is from JUnit 5.