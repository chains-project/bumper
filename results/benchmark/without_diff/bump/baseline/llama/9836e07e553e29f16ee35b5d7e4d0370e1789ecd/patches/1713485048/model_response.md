Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "pulling image")
    );
}
```
The `StringContains` constructor taking a single `String` argument is not applicable due to the error message, so we're using the `AllOf` class from the Hamcrest library to combine two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the given image name, while the second `StringContains` matcher checks for the presence of the string "pulling image".

By combining these two matchers using the `AllOf` class, we can create a single matcher that matches both conditions, which should fix the error.