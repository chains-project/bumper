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
                " pulling image " + image + " latest"
            )
        );
    }
```
The `StringContains` constructor takes two parameters: the first is a `String` that represents the containing string, and the second is a `String` that represents the contained string. In the original code, the second parameter is a formatted string that includes the image name.

The error message indicates that the `StringContains` constructor cannot be applied to the given types, which means that the second parameter is not a `String`. To fix this, we can replace the second parameter with a `String.format` call that includes the image name as a variable:
```scss
String.format(" pulling image %s latest", image)
```
By doing this, we ensure that the second parameter is a `String`, and the `StringContains` constructor can be applied successfully.

Additionally, we can simplify the code by using the `AllOf` class from the Hamcrest library, which allows us to combine multiple matchers into a single matcher. In this case, we can use `AllOf` to combine the two `StringContains` matchers, which makes the code more concise and easier to read.

Therefore, the proposed patch replaces the original `imagePulled` method with the updated version that uses `AllOf` and formats the second parameter of the `StringContains` constructor as a string.