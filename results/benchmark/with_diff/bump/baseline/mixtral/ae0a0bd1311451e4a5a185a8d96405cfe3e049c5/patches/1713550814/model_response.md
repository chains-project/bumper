Here's the fixed version of the `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    String contains = String.format("Status: Downloaded newer image for %s", image);
    return new StringContains(contains);
}
```
The issue was that the `StringContains` constructor was being called with two arguments, but it only accepts one argument in the new library version. To fix this, I created a new variable `contains` to store the string that we want to check for, and then passed it as the only argument to the `StringContains` constructor.