Here's the proposed patch to fix the error:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```

In the original code, the problem is that the `containsString` method expects a `CharSequence` argument, but `String.format` returns a `String`. To fix this, we can first format the message and assign it to a separate variable, and then pass it as an argument to `containsString`.