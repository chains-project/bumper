Here's the proposed patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```

The change includes storing the string format result in a separate variable, which should resolve the error message.