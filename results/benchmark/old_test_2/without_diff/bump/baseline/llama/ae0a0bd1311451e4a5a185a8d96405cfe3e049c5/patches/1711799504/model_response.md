Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            false,
            "pullImage"
        )
    );
}
```
This patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first one checks for the presence of the given image name in the output, and the second one checks for the presence of the string "pullImage". This should fix the error by providing a different way to match the output.

Note that I've also removed the `Override` annotation, as it's not needed in this case.