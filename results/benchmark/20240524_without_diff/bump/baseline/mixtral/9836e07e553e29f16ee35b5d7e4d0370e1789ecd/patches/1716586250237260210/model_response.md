Here is the proposed patch:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```

This patch removes the unnecessary inner `containsString` call and directly passes the formatted message to the `containsString` method. This should resolve the "identifier expected" error.