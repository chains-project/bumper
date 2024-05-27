Here is a possible patch for the code:
```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_round() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```
The patch changes the `assumeTrue` method to `assertTrue`, which is the equivalent method in JUnit 5.
The `import static` statements are added to import the static methods of `Assertions` class.
This patch assumes that the `GROUP_SHAPE` variable is defined and accessible in the scope of the test method.