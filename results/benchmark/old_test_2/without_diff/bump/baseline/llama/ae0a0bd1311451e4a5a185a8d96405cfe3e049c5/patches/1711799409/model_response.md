Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
The `StringContains` constructor taking two parameters is not available in the version of the Hamcrest library being used. We can work around this by creating a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of the given image name, and the second `StringContains` matcher checks for the presence of the success message.