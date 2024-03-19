I understand that you want a fixed version of the `imagePulled` method, I am assuming that the failure is caused by an updated Hamcrest version that has changed the `StringContains` constructor's parameters.

Based on the error message, it seems that the constructor `StringContains(boolean, String)` is no longer available. I will replace the usage of `StringContains` with `StringStartsWith` and `StringContainsIgnoringCase` to make it work with the new Hamcrest version.

Here's the updated method:
```java
private static Matcher<String> imagePulled(final String image) {
    if (image.startsWith("sha256:")) {
        return new StringStartsWith(String.format("Status: Downloaded newer image for %s", image));
    } else {
        return new StringContainsIgnoringCase(String.format("Status: Downloaded newer image for %s", image));
    }
}
```
This new version of the method checks if the image starts with "sha256:". If it does, the method uses `StringStartsWith`; otherwise, it uses `StringContainsIgnoringCase`. This should resolve the issue with the updated Hamcrest library.