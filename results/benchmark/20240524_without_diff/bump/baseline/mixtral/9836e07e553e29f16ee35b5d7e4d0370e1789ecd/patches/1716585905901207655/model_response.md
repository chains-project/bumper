Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch uses the `containsString` method from the `CoreMatchers` class, which is an added library method identified with `++`. The `CoreMatchers` class provides a rich set of matchers for Hamcrest, which can be used to match against various types of objects. In this case, the `containsString` method is used to check if a string contains a specific substring. This should fix the error caused by the failure to apply the `StringContains` constructor.