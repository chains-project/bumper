Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Status: Downloaded newer image for %s", image) + "%"
    );
}
```
The patch adds a `%` at the end of the format string to avoid a compilation error.

It's important to note that this patch doesn't address the root cause of the issue, which is likely a version conflict between the `org.hamcrest:hamcrest-core` and `org.hamcrest:hamcrest-library` dependencies. The `StringContains` constructor that takes a single argument was removed in version 2.0 of the `hamcrest-core` library, which is likely being used in the project.

To resolve the issue, you may need to upgrade the version of `org.hamcrest:hamcrest-library` to a version that includes the removed constructor, or modify the code to use a different method to achieve the desired result.