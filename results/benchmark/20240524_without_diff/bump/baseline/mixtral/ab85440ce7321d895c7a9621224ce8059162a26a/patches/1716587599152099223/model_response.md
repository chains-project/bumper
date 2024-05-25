Sure, here's a potential patch for the failing code:
```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```
In this patch, I created a new variable `message` to store the formatted string, and then passed it as an argument to `CoreMatchers.containsString()`. This should resolve the "identifier expected" error.