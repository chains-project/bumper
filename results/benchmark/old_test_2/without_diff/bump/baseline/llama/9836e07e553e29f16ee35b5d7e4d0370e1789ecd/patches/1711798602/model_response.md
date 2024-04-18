Here's a possible patch to fix the error:
```
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringEndsWith(image)
    );
}
```
This patch replaces the `StringContains` constructor with the `AllOf` class from the same library, which allows combining multiple matchers using the `and` method. The `StringEndsWith` matcher is used to check if the output string ends with the image name, which should be sufficient to replace the `StringContains` matcher.

It's important to note that this patch doesn't address the root cause of the error, which is likely a version conflict between the `hamcrest` and `docker-adapter` dependencies. The patch only provides a temporary solution to make the test pass, but it's recommended to resolve the version conflict as well.