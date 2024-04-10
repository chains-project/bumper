Here's a possible patch to fix the error:
```diff
-@org.junit.jupiter.api.Test
-@micycle.pgs.Ignore
+@org.junit.jupiter.api.Test
+@micycle.pgs.Test
void testRobustnessRandomly() {
    // ...
}
```
The patch removes the `micycle.pgs.Ignore` annotation, which is not recognized in the new library version, and adds the `micycle.pgs.Test` annotation instead. This should allow the test to run without any issues.

Note that this patch assumes that the `micycle.pgs.Test` annotation is available in the new library version. If it's not available, you may need to use a different annotation or modify the test class accordingly.