Here is a fixed version of the method using a `contains` method from the `org.hamcrest.CoreMatchers` class to check if the string contains the specified substring:
```java
private static Matcher<String> imagePulled(final String image) {
    return CoreMatchers.containsString(
            String.format("Downloaded newer image for %s", image)
    );
}
```
This version of the method should work even if the `StringContains` class is no longer available.