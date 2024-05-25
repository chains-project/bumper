Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch replaces the `StringContains` constructor with a call to `CoreMatchers.containsString`, which is a new method added in Hamcrest version 2.1. The `CoreMatchers` class provides a set of matchers that can be used to match against various types of objects, including strings. The `containsString` method checks if a string contains a given substring, which is what the original code was trying to do.

Note that the `CoreMatchers` class is part of the Hamcrest library, so it should be available in the project's classpath. If it is not, you may need to add a dependency to the Hamcrest library in your project's build configuration.