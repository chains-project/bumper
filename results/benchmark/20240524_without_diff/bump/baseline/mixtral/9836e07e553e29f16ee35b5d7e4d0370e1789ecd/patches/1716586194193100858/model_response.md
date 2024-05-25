Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In the original code, the `StringContains` class is used from the `org.hamcrest.core` package, which seems to be causing the error. The `CoreMatchers` class from the same package provides a similar method called `containsString`, which can be used instead. This should fix the error and make the code work as intended.