Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            true,
            "pullImage"
        )
    );
}
```
The `StringContains` constructor taking a single `String` argument has been removed in the latest version of the Hamcrest library. To fix the error, we can replace it with the `AllOf` class, which is a part of the Hamcrest library as well. The `AllOf` class takes an iterable of matchers as its constructor argument, and it matches if all of the contained matchers match.

In this case, we create an `AllOf` matcher that contains two `StringContains` matchers. The first one checks for the presence of the string "Status: Downloaded newer image for" followed by the image name, and the second one checks for the presence of the string "pullImage". The `AllOf` matcher will only match if both of these conditions are met.

Note that we've also removed the `Override` annotation, as it's not needed in this case.