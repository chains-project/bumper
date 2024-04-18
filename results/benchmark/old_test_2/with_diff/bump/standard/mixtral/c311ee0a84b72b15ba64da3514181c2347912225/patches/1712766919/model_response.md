Here is the proposed patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

In the updated library version, the `StringContains` constructor has been removed and replaced with the `containsString` method in the `Matchers` class. The new method only takes a single argument, which is the substring to search for. The `String.format` method is used to construct the expected substring, which includes the input image string.