Here is the patched version of your code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.containsString(
        java.lang.String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In the new version of the library, the `StringContains` constructor has been removed and replaced with a method called `containsString`. The `containsString` method only takes a single argument, which is the string to search for. I have updated the code to use this method instead.