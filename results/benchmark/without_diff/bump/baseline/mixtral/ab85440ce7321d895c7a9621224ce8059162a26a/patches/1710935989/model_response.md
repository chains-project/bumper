I understand that you're asking for help in fixing the failing test in the `CachingProxyITCase` class, particularly the `imagePulled` method. The error message indicates that there's a problem with the usage of the `StringContains` constructor.

To fix this issue, I suggest using `CoreMatchers.containsString` instead of `StringContains`. Here's the updated code:

```java
private static Matcher<String> imagePulled(final String image) {
    return CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch should resolve the error and enable the test to compile and run successfully.