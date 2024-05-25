Here is a possible patch for the code you provided:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```
The issue with the original code is that the `containsString` method expects a `CharSequence` as its argument, but `String.format` returns a `String`. By assigning the result of `String.format` to a separate variable and passing that variable to `containsString`, the issue is resolved.