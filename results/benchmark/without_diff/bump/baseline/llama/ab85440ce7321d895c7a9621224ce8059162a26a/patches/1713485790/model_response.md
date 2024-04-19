Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            false,
            " Pulled"
        )
    );
}
```
The `StringContains` constructor takes two parameters, a `pattern` and a `message`, and it expects the `pattern` to be a regular expression. In the original code, the second argument is a string that doesn't match the expected pattern, causing the compiler error.

The patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers into a single matcher. The first matcher is the same as before, but the second matcher is a new `StringContains` instance that looks for the string " Pulled". This should fix the compiler error and make the code compile without issues.