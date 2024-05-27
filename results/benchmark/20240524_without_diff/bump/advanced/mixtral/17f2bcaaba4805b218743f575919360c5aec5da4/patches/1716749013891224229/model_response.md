Here is the fixed version of the code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, out.getChildCount());
}
```

The error message suggests that the method `assumeTrue` cannot be found. This is because the import statement for the method is missing. I added the import statement `import static org.junit.jupiter.api.Assumptions.assumeTrue;` to fix the error.

Note: I also added the import statement `import static org.junit.jupiter.api.Assertions.assertEquals;` to make the code more concise and easier to read. This import statement was not necessary to fix the error.