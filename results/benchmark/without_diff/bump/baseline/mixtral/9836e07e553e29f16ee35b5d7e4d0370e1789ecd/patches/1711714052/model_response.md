Here is a fixed version of the method using a different Hamcrest matcher, `StringStartsWith`, instead of `StringContains`:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringStartsWith(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
This version of the method should work as long as the error message always starts with the string "Status: Downloaded newer image for " followed by the image name. If the error message format changes, this matcher may need to be updated accordingly.