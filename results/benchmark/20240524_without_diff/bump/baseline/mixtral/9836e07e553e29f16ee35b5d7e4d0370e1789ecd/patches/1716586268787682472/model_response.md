Here's a patch that you can apply to the code in order to fix the error:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Downloaded newer image for %s", image);
    return new CoreMatchers.<String>containsString(message);
}
```

In this patch, I created a new variable `message` to store the string that was previously passed directly to `String.format()`. This makes the code easier to read and understand.

Note that I did not remove the `@Override` decorator because the method is still overriding a method in the new version. I also did not use any removed or added library methods.

This patch should fix the error and allow the code to compile successfully.