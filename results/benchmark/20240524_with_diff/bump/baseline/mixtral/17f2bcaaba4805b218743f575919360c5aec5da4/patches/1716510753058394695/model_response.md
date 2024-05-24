Here's the proposed patch:
```java
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

@RunWith(Enclosed.class)
public class FastPolygonizerTests {
    // existing test classes go here
}
```
In the original code, the `@Ignore` annotation is used to ignore a test class or a test method. However, the `@Ignore` annotation has been removed in the new version of the library.

To fix the error, we can use the `@RunWith` annotation with `Enclosed` runner instead of using `@Ignore` annotation. The `Enclosed` runner allows us to run all the inner classes as tests, which effectively ignores any test class that we don't want to run.

Note that the `@RunWith` annotation should be added to the outermost class of the test suite, not the individual test classes.