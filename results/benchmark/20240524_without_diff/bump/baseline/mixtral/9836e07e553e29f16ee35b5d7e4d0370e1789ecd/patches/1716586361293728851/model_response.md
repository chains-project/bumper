Here is a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String msg = String.format("Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(msg);
}
```

This patch removes the unnecessary inner class declaration of `CoreMatchers.<String>containsString` and assigns its result to a variable `msg`, which is then passed to the `containsString` method. This should fix the "identifier expected" error.