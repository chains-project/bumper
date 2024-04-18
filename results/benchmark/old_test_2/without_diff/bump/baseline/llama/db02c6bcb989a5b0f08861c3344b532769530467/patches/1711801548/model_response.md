Here's a possible patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Image pulled successfully")
    );
}
```
The `StringContains` constructor taking a single `String` argument is not available in the version of the Hamcrest library being used. We can work around this by using the `AllOf` class from Hamcrest, which allows us to combine multiple matchers using the `and` method. We create two `StringContains` matchers and combine them using `AllOf`. The first `StringContains` matcher checks for the presence of the given image name in the output, and the second matcher checks for the presence of the phrase "Image pulled successfully".

This patch replaces the entire failing client code, does not change the function signature, and does not use any removed library methods.