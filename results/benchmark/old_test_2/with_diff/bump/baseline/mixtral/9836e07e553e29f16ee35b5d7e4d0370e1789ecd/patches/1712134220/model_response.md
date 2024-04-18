Here is a possible patch for the failing code:
```java
private static Matcher<String> imagePulled(final String image) {
    String matchString = String.format("Downloaded newer image for %s", image);
    return new StringContains(matchString);
}
```
In this patch, we create a separate variable `matchString` to store the substring we want to match against. Then, we pass this variable as the argument to the `StringContains` constructor, which now only takes a single `String` argument. This should resolve the error message you were seeing, which indicated that the constructor was expecting a single `String` argument, but received a `boolean` and a `String` instead.