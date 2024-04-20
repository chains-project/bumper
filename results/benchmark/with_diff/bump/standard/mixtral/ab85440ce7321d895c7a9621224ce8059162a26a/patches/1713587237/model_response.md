Here's the fixed version of the method. I added a local variable `message` to store the status message string and used it in the `StringContains` constructor.

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    final String message = String.format("Status: Downloaded newer image for %s", image);
    return new org.hamcrest.core.StringContains(org.hamcrest.core.StringContains.containsString(message));
}
```

This fixes the ';' expected error by removing the unnecessary semicolon in the `containsString` method call and using a local variable for the status message.