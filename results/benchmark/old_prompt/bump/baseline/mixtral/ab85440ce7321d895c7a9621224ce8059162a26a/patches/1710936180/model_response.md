Here is a potential patch for the failing client code:
```java
private static Matcher<String> imagePulled(final String image) {
    String expectedLogMessage = String.format("Downloaded newer image for %s", image);
    return is(containsString(expectedLogMessage));
}
```
The original code was checking if the log message contained the string `"Status: Downloaded newer image for <image>"` but the error message suggests that there is no `';'` after `"Status: "`. To fix this issue, I have created a separate variable `expectedLogMessage` that stores the expected log message without the `"Status: "` prefix. The `Matcher` is then created using this variable.

This patch does not change the function signature or use any removed library methods. It creates a new variable `expectedLogMessage` to make the code easier to understand and to avoid the error.