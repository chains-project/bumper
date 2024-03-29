Here is a fixed version of the method using a `contains` method from `StringUtils` class which is an added method in the latest version of the library:

```java
private static Matcher<String> imagePulled(final String image) {
    String targetMessage = String.format("Status: Downloaded newer image for %s", image);
    return new StringContains(false, StringUtils.contains(targetMessage, image));
}
```
Note: `StringUtils` class is a part of `org.apache.commons-lang3` library. Make sure to include the library as a dependency in your project.