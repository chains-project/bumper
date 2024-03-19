I understand that you want me to fix the failing Java method using only compatible changes to the existing code, while only using Hamcrest methods that are present in the version I am working with (no removed methods). Here is my proposed fix:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.StringContains(
        CoreMatchers.is(String.format("Status: Downloaded newer image for %s", image))
    );
}
```

In this patch, I replaced the usage of `StringContains` from `org.hamcrest.core` with `CoreMatchers.StringContains` from `org.hamcrest.CoreMatchers`, which is the new location of the class in the updated version of Hamcrest. I also added a call to `CoreMatchers.is()` to wrap the string format, since the `StringContains` constructor now expects a `Matcher<String>` instead of a `String`.