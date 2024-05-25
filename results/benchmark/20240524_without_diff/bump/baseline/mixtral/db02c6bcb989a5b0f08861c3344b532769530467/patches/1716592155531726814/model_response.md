Here's a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor with the `CoreMatchers.containsString` method, which is a new method added in Hamcrest 2.1. The `CoreMatchers` class is part of the Hamcrest library and provides a set of matchers that can be used for testing.

By using `CoreMatchers.containsString`, we can avoid the error caused by the deprecated `StringContains` constructor. This should fix the error and allow the code to compile and run successfully.