Here's the patched version of the code that should fix the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

The error message indicates that the `StringContains` constructor now requires only one argument, whereas previously it accepted two arguments. Therefore, we need to modify the code to pass only one argument to the constructor.

In the new library version, the `StringContains` class has a constructor that takes a single `String` argument, which is the substring to search for in the target string. Therefore, we can create an instance of `StringContains` by passing the target substring as the argument.

Note that we need to use the fully qualified name of the `StringContains` constructor, i.e., `org.hamcrest.core.StringContains.StringContains`, because the `StringContains` class is now generic and has multiple constructors with different argument lists.