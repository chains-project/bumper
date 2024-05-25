Here is a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, I replaced the `StringContains` class from the `org.hamcrest.core` package with the `containsString` method from the `CoreMatchers` class in the same package. This should fix the error message you provided.

Note that this patch assumes that the `CoreMatchers` class is available in the project's classpath. If this is not the case, you may need to add the appropriate dependency to your project's configuration.