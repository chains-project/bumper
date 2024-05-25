Here's a possible patch for the code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.<String>containsString(
            String.format("Downloaded newer image for %s", image)
    );
}
```
In this patch, we're using the `containsString` method from the `CoreMatchers` class, which is an added method in newer versions of Hamcrest. This method can be used as a replacement for the deprecated `StringContains` constructor that was causing the compilation error.