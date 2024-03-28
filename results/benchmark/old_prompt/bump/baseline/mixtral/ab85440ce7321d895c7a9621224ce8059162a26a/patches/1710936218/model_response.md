Here's a patch for the failing method. It looks like there is a missing parenthesis in the original code, which is causing the error.
```java
private static Matcher<String> imagePulled(final String image) {
    return is(containsString(String.format("Status: Downloaded newer image for %s", image)));
}
```
However, since the error message suggests that there is an issue with a line of code that references this method (`CachingProxyITCase.java:[171,93]`), it's possible that there is an issue with how this method is being called. Here's an example of how this method might be called:
```java
assertThat(response, imagePulled("my-image"));
```
Make sure that the argument to `imagePulled` is a string, and that there are no syntax errors in the surrounding code.