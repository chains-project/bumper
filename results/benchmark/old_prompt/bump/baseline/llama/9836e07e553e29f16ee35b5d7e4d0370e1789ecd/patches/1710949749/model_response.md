Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, "Pulling image " + image + " failed")
    );
}
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the image name.

The error message indicates that the constructor cannot be applied to the given types, which means that the image name is being passed as a `String` instead of a `CharSequence`. To fix this, we can use the `String.format` method to format the string with the image name as a argument, like this:
```java
String.format("Status: Downloaded newer image for %s", image)
```
This will create a new `String` object that contains the formatted string with the image name as a argument, which can be passed to the `StringContains` constructor.

Additionally, we can simplify the code by using the `AllOf` class from the Hamcrest library, which allows us to combine multiple matchers into a single matcher. In this case, we can use `AllOf` to combine the two `StringContains` matchers into a single matcher that matches both conditions.