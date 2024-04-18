Here is a fixed version of the method, assuming that the goal is to check if the downloaded image's name is the same as the `image` argument:
```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return new StringContains(false, message).matches(message);
}
```
The `matches` method of `StringContains` matcher is used to check if the provided string matches the expected substring.

Note: This code assumes that the `StringContains` class and its `matches` method are still available and unchanged in the new version of the external dependency. If this is not the case, the solution may need to be adjusted accordingly.