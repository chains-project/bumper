Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
This patch replaces the `StringContains` class with the `AllOf` class, which is also from the Hamcrest library. The `AllOf` class takes an array of matchers as its constructor argument and matches when all of the matchers match. In this case, we create an array of two matchers: the first one looks for the string "Status: Downloaded newer image for " followed by the image name, and the second one looks for the string "Image pulled successfully".

The `StringContains` class is not needed in this case because the `AllOf` class can handle multiple matchers. Additionally, the `StringContains` class has been deprecated in favor of the `AllOf` class.

This patch should fix the error and make the code compile-time ready.