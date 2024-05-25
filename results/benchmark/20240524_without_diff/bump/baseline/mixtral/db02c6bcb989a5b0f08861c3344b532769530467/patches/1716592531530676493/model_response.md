Here's a possible patch that you can apply to the code to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, I replaced the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class. This method is an added library method identified with `++`, and it can be used as a replacement for the `StringContains` constructor.