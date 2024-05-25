Here is a possible patch for the `imagePulled` method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.StringContains(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` constructor from the `org.hamcrest.core` package with the one from the `org.hamcrest.CoreMatchers` package. This is because the `StringContains` constructor from `org.hamcrest.core` has been removed in the new version, and has been moved to the `org.hamcrest.CoreMatchers` package.

Note that this patch assumes that the `CoreMatchers` class is available in the classpath. If it is not, you may need to add a dependency to the `hamcrest-library` module in your build tool configuration.