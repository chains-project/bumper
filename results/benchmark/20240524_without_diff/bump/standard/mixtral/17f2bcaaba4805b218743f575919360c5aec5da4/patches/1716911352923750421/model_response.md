Here's the proposed patch to fix the error:

```java
import micycle.pgs.commons.TestIgnore;

@org.junit.jupiter.api.Test
@TestIgnore
void testRobustnessRandomly() {
    // ... (rest of the method remains unchanged)
}
```

This patch imports the `TestIgnore` annotation from `micycle.pgs.commons` package and uses it in the method. This should resolve the "cannot find symbol" error.