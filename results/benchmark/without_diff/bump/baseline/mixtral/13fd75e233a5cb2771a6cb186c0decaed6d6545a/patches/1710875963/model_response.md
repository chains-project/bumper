I understand that you want a fixed version of the `imagePulled` method, and I will assume that the `StringContains` class and the `override` keyword are from Hamcrest library. Based on the error message, it seems that the constructor for `StringContains` with a single `String` argument no longer exists in the version of Hamcrest you're using. I will assume that the closest alternative constructor is the one with two `String` arguments, where the second argument is the `String` to search for.

Here's the fixed `imagePulled` method that should resolve the error:

```java
private static Matcher<String> imagePulled(final String image) {
    String searchString = String.format("Downloaded newer image for %s", image);
    return new StringContains(
            false,
            searchString, 
            searchString
    );
}
```

In this fixed version, the `StringContains` constructor with two `String` arguments is used. The first `String` argument is set to `false` to indicate a negative matcher, while the second one is the `searchString` which is the same as before.

This should resolve the compilation error you are facing.