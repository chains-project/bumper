Here's the fixed `imagePulled` method:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```
In the original code, the `StringContains` constructor was being called with two arguments, but it only accepts one argument. I replaced it with the `containsString` method from `CoreMatchers`, which accepts a single `String` argument.