Here is a possible patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

@Test
void test_PGS_Morphology_smooth() {
    assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

The patch changes the `assumeTrue` method to `assertTrue`, which is the equivalent method in JUnit 5. The `assumeTrue` method is part of JUnit 4, and it is not available in JUnit 5. The `assertTrue` method checks that the condition is true, and if it is not, it fails the test and reports an error message.

I hope this helps! Let me know if you have any other questions.