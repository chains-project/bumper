Sure, I understand the requirements. Here's a fixed version of the method that should resolve the compilation error:
```java
private static Matcher<String> imagePulled(final String image) {
    boolean containsImage = StringUtils.contains(String.format("Status: Downloaded newer image for %s", image), "Status: Downloaded newer image for ");
    return new StringContains(false, containsImage);
}
```
In this version, I've created a separate variable `containsImage` to store the result of the `StringUtils.contains` method, and then passed that variable to the `StringContains` constructor. This should resolve the compilation error by ensuring that the expression passed to `new StringContains` is a valid boolean value.