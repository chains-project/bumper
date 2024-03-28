Here's a patch for the failing method. It seems like there's a missing closing parenthesis in the `is` method call, which I added:

```java
private static Matcher<String> imagePulled(final String image) {
  return is(containsString(String.format("Status: Downloaded newer image for %s", image))); // added ) here
}
```

However, if the error message is about a missing semicolon, then it might be in the test code. Nonetheless, I cannot access the test code or the complete class, so here's the fixed version of the provided method.