Here's a possible patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

Becomes:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, java.lang.String.format("Status: Downloaded newer image for %s", image), org.hamcrest.core.IsEqual.equalTo(true));
}
```
The `StringContains` constructor that takes a single `String` argument has been removed in the new library version, so we need to use the variant that takes two `String` arguments instead. We also need to add a third argument of type `org.hamcrest.core.IsEqual` to make the matcher more specific.