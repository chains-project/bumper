Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
The `StringContains` constructor takes two parameters, a `boolean` and a `String`, and checks if the string contains the given substring. However, in this case, the second parameter is a formatted string that includes the image name, which is not what `StringContains` is intended for.

Instead, we can use `AllOf` to combine two matchers: `StringContains` with the formatted string and `StringEndsWith` with the image name. This way, the matcher will succeed if the string contains the formatted string and ends with the image name.

Note that I removed the `Override` annotation, as it's not necessary in this case.