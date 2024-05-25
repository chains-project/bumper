Here's a possible patch for the code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
In this patch, we're using the `containsString` method from the `CoreMatchers` class instead of the `StringContains` constructor. This method is available in Hamcrest 2.2, which is a later version than the one causing the error.