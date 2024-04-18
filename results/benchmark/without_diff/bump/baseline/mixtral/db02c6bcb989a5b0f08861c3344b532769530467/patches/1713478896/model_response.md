Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor from the `org.hamcrest.core` package with the `containsString` method from the `org.hamcrest.CoreMatchers` package. This is because the `StringContains` constructor has been removed in the new version of the library, and has been replaced with the `containsString` method.

Note that this patch assumes that the `CoreMatchers` class is available in the classpath. If this is not the case, you may need to import the class at the beginning of the file.

I hope this helps! Let me know if you have any questions.