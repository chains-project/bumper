Here's the proposed patch:

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

The `assumeTrue` method is from JUnit 4 and is not available in JUnit 5, which the code seems to be using based on the import statement `import org.junit.jupiter.api.Test;`. The `assertTrue` method from JUnit 5 can be used instead.