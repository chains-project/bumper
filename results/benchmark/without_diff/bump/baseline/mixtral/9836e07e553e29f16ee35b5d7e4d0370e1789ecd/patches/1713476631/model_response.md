Here is a potential patch for the failing code:
```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```
I removed the `new` keyword before `CoreMatchers` and assigned the string to a variable `message` before passing it to `containsString`. This should resolve the "identifier expected" error.