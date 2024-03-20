Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(
                false,
                String.format("Status: Downloaded newer image for %s", image)
            ),
            new StringContains(
                true,
                " pulling image " + image + " latest"
            )
        );
    }
```
The error message indicates that the `StringContains` constructor cannot be applied to the given types. This is because `StringContains` expects a single string argument representing the expected substring, but the code passes two string arguments.

The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers into a single matcher. The first argument to `AllOf` is a `StringContains` matcher that looks for the substring "Downloaded newer image for" followed by the image name. The second argument is another `StringContains` matcher that looks for the substring " pulling image " followed by the image name.

This should fix the error and allow the code to compile.