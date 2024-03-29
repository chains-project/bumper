Here's a possible patch to fix the failing code:
```java
private static Matcher<String> imagePulled(final String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return new StringContains(false, message, message);
}
```
In this patch, we create a new `StringContains` instance using the `message` variable for both the `subString` and `containing` parameters. This ensures that the `StringContains` constructor is called with the correct types.

We also added a third parameter `containing` which was added in a newer version of Hamcrest. This parameter is not used in this case, but it's required by the constructor.

This patch should fix the compilation error and allow the code to run successfully.