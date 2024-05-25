Sure, I understand the requirements. Here is a patch that you can apply to the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```
The issue with the original code is that the `containsString` method expects a `CharSequence` as its argument, but `String.format` returns a `String`. To fix this, I have created a separate variable `message` to store the formatted string, and then passed this variable as an argument to `containsString`. This should resolve the compilation error.