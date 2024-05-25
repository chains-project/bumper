Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String msg = String.format("Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(msg);
}
```

In this patch, we store the formatted string in a separate variable `msg` before passing it to `CoreMatchers.containsString()`. This avoids the need for nested method calls, which was causing the "identifier expected" error.