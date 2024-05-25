Here is a possible patch for the given code:
```java
private static Matcher<String> imagePulled(final String image) {
    String msg = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(msg);
}
```
This patch creates a temporary variable `msg` to store the formatted string, which should resolve the "identifier expected" error.