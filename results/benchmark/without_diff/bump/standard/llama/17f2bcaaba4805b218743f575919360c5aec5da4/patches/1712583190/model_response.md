It seems that the `Ignore` class is not available in the current context. You can fix this issue by adding the necessary dependencies to your project or by using a different way to ignore the test.

Here's a patch that you can apply to the code to fix the error:
```diff
- @org.junit.jupiter.api.Test
- @micycle.pgs.Ignore
+ @org.junit.jupiter.api.Test
+ @org.junit.jupiter.api.Ignore
void testRobustnessRandomly() {
    // rest of the code remains the same
```
In this patch, we've replaced the `micycle.pgs.Ignore` annotation with `org.junit.jupiter.api.Ignore`. This should fix the error and allow the test to run correctly.