Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ),
        new StringContains(
            false,
            " Pulled"
        )
    );
}
```
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of " Pulled". By combining these two matchers with `AllOf`, the method should pass even if the " Pulled" string appears after the image name.


This patch does not change the method signature, and it removes the `Override` annotation since it's not necessary. It also uses the `StringContains` class from the Hamcrest library, which is available in the Java 8 SDK.