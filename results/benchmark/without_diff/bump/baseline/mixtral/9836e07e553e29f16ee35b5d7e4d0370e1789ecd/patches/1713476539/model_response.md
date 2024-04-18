Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```
In this patch, I created a new variable `message` to store the string to be matched. This makes the code easier to read and understand. Other than that, the code is the same as the original.