Here's a possible patch for the given code:

```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return CoreMatchers.<String>containsString(message);
}
```

In this patch, I removed the unnecessary `new` keyword when creating the `CoreMatchers.<String>containsString` matcher. It looks like the Java compiler was confused by the syntax and expected an identifier instead. By removing the `new` keyword, the code becomes clearer and easier to read.