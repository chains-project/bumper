Here's a possible patch to fix the failing code:
```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return new StringContains(false, message);
}
```
In this patch, we first create a new variable `message` to store the expected log message. Then, we pass this variable as an argument to the `StringContains` constructor. This way, we avoid calling the `String.contains()` method directly and instead use the `StringContains` matcher to check if the log message contains the expected substring. This should fix the error caused by the `StringContains` constructor not accepting a `String` argument directly.