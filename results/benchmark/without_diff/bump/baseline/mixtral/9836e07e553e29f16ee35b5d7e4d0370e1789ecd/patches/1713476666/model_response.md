Here's a proposed patch to fix the error:

```java
private static Matcher<String> imagePulled(final String image) {
    String msg = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(msg);
}
```

The issue was with the extra angle brackets in the `CoreMatchers` method call. I've created a temporary variable `msg` to make the code easier to read.